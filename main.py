from fastapi import FastAPI, Depends, HTTPException
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define all the Google API scopes that we have enabled in cloud for accessing spreadsheets, Drive
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    "openid",
    "https://www.googleapis.com/auth/userinfo.profile",
    "https://www.googleapis.com/auth/userinfo.email"
]

app = FastAPI() # Create a FastAPI application instance

# Include the spreadsheet ID that we used for storing the Users data
MY_SPREADSHEET_ID = '1LK-m9g23v7L37-ZO8ZZ55EV7t1sUNsmSmH_vD3QOxnU'

# Set up the OAuth 2.0 flow with the client secrets file and scopes
flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)

# Function to get the authenticated Google Sheets service
def get_service():
    creds = None
    if os.path.exists("token.json"):  # Check if the token file exists
        # Load credentials from the token file
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If credentials are not valid or do not exist, refresh or prompt for login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds = flow.run_local_server(port=8081)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
        
    # Build the Google Sheets API service using the credentials
    service = build('sheets', 'v4', credentials=creds)
    return service  # Return the service object

# Endpoint get users spread sheet data and insert into Owner spreadsheet data
@app.get("/spreadsheets")
def list_spreadsheets(user_spreadsheet_id: str, user_range: str):
    service = get_service()
    
    # Fetch data from the user's spreadsheet
    user_sheet = service.spreadsheets()
    user_result = user_sheet.values().get(spreadsheetId=user_spreadsheet_id, range=user_range).execute()
    user_values = user_result.get("values", [])
    
    if not user_values:
        raise HTTPException(status_code=404, detail="No data found in the user's spreadsheet")
    
    # Insert the user's data into Owner spreadsheet
    my_sheet = service.spreadsheets()
    body = {
        "values": user_values
    }

    my_sheet.values().append(
    spreadsheetId=MY_SPREADSHEET_ID,
    range="Sheet1",  
    valueInputOption="RAW",
    insertDataOption="INSERT_ROWS",
    body=body
    ).execute()
    os.remove('token.json')
    
    return {"message": "Data inserted successfully into your spreadsheet"}

# End point to notify users to accepts company policies
@app.get('/privacy-policy')
def privacy_policy():
    Message = "This is Application can access your Google Sheets Data. If you want to share your data click on to continue"
    return Message

@app.get('/')
def root():
    Message = {"Application was running"}
    return Message