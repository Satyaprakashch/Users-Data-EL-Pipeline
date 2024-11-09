# Documentation for the EL Pipeline Project Using FastAPI, Google Cloud Console, Airbyte and AWS S3

This documentation provides a comprehensive guide to setting up and running an Extract and Load (EL) Pipeline using FastAPI, Google Cloud console, Airbyte and AWS S3.

# Table of Contents
#### 1. Project Overview
#### 2. Prerequisites
#### 3. Google Cloud Project Setup
#### 4. Google Sheets API Setup
#### 5. AWS S3 and IAM Configuration 
#### 6. Project Structure
#### 7. Code Explanation
#### 8. Running the Project
#### 9. API Endpoint Details
#### 10. Airbyte Setup and Configuration

### 1. Project Overview:
This FastAPI application allows users to authenticate using their Google accounts, access their Google Sheets data, and append this data to a pre-defined spreadsheet in Google Sheets. Created El(Extract Load) Scheduled Pipeline using Airbyte to sync this Spreadsheet Data to AWS S3.

### 2. Prerequisites
  Python 3.8 or higher<br>
  Google Cloud account<br>
  AWS account with S3 access<br>
  Airbyte instance for data synchronization<br>

### 3. Google Cloud Project Setup
#### Create a Google Cloud Project:
a. Go to Google Cloud Console.<br>
b. Click on New Project and create a new project.<br>

#### Enable Google Drive APIs:
a. In the Google Cloud Console, navigate to APIs & Services > Library.<br>
b. Enable the Google Drive API.<br>

#### Create OAuth Credentials:
a. Go to APIs & Services > Credentials.<br>
b. Click on Create Credentials > OAuth client ID.<br>
c. Share required details like Developer Contact Information.<br>
d. Add the required scopes for the application like ['auth/drive', 'auth/spreadsheets, 'auth/userinfo.profile]<br>
e. Select Web application type as "Web Application" in Oauth Client ID<br>
f. In the Authorised JavaScript Origins give the homepage URI Adress and in the Authorised Redirecr URIs List the URIs that you use for this application.<br>
j. Atlast Download the credentials in JSON Format<br>
Some Pictures When Developing the Project:<br> 

![image](https://github.com/user-attachments/assets/05000e72-1aff-4e5a-8b50-d857074a980c)
<br> 
![image](https://github.com/user-attachments/assets/a386022d-89b7-4c81-b813-54cf913e09fd)

#### Enable Google Sheets APIs:
a. In the Google Cloud Console, navigate to APIs & Services > Library.<br>
b. Enable the Google Sheets API.<br>

####  4. Google Sheets API Setup
##### Prepare the Spreadsheet:
a. Open Google Sheets and create or use an existing spreadsheet and Note the spreadsheet ID (found in the URL of the sheet).<br>
b. Place the downloaded credentials.json in the project drirectory. This file will be used for OAuth 2.0 authentication.<br>

#### 5. AWS S3 and IAM Configuration 
##### Create S3 Account
a. Locate to Amazon S3 > Buckets > Create bucket in AWS Console<br>
b. Create S3 bucket in AWS. Choose the Bucket type - General Purpose<br>
c. Block all Public access for security reasons.<br>
d. Enable Server-side encryption with Amazon S3.<br>

##### IAM Configuration for Airbyte
a. Locate to IAM > Users > Create user in AWS Console.<br>
b. Give the user a Name.<br>
c. Attach necessary policies to this User so Airbyte can access and write the data to S3.<br> 
d. Use the below Json Document to create the policy.<br>
e. Locate to IAM > Users > Username > Security credentials<br>
f. Create the Access key and download it locally To connect Airbyte to S3.<br>
![image](https://github.com/user-attachments/assets/9afda3e9-398b-45ca-b230-5995f23e8f1c)

#### 6. Project Structure:
/project-root<br>
│<br>
├── main.py &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # FastAPI application code<br>
├── credentials.json &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # Google OAuth credentials<br>
├── token.json &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # OAuth token (generated automatically when user logged in using google acc)<br>
└── requirements.txt &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # Python dependencies<br>

#### 7. Code Explanation
###### The main components of the code are as follows:
Imports: The necessary libraries are imported, including FastAPI, Google authentication libraries, and Pydantic for data validation.
SCOPES: Define scopes required for accessing Google Sheets and user information.
MY_SPREADSHEET_ID: Give Your Spreadsheet ID, this spreadsheet will save all the users data.
FastAPI Instance: An instance of FastAPI is created.
get_service() Function: This function handles authentication and returns a service object to interact with Google Sheets API.
list_spreadsheets Endpoint: This endpoint retrieves data from a user's spreadsheet and appends it to a predefined spreadsheet.

#### 8. Running the Project

1) Clone repository into your machine

```md
git clone 
cd Users-Data-EL-Pipeline
```
2) Creating a virtual environment

```md
python -m venv venv
```

2.Activating it

a) Using CMD

```md
.\venv\Scripts\activate.bat
```

b) Using PowerShell

```md
.\venv\Scripts\Activate.ps1
```
3.Installing dependencies

```md
pip install -r requirements.txt
```
4) Run app

```md
uvicorn main:app --reload
```

#### 9. API Endpoint Details:

##### a. GET /spreadsheets
Parameters:
user_spreadsheet_id: The ID of the user's spreadsheet to fetch data from.
user_range: The cell range to extract data (e.g., "A1:D10).
Description: This endpoint retrieves data from a user's specified Google Sheets document and inserts that data into the owner’s predefined Google Sheets document.
Response: A success message if data is inserted successfully.
##### b. GET /privacy-policy
Description: Returns a message that informs the user about the app’s access policy and prompts them to agree if they wish to proceed.
Response: A string message explaining the data access policy.
##### c. GET /
Description: A simple root endpoint to check if the application is running.
Response: A dictionary with the message "Application was running".
##### d. Swagger UI (Give you detailed documentation about the end Points)
    ```linux
    http://localhost:8000/docs
    ```
    
#### 10. Airbyte Setup and Configuration:
###### 1. Setup Google sheets as Source
a. In Airbyte Source select Google Sheets as Source
b. Authenticate with Google Oauth2.0 that we have already configured in our Google Project.
c. Copy your spreadsheet link that contains the users data.
d. Test the Source
![image](https://github.com/user-attachments/assets/41406554-6755-4c3c-a765-c93f8bc0a3b8)

###### 2. Setup S3 as Destination
a. In Airbyte destination select S3 as Destination.
b. Configure Destination with your AWS Access key ID, Secret Access key
c. Give your AWS S3 Bucket name, Bucket path and Bucket region that you have already created in AWS 
d. Test the destination
![image](https://github.com/user-attachments/assets/e009785f-9471-4fdb-84b1-8be9733024f3)

###### 3. Create the Connection between Source and Destination
a. Select the existing Google sheets as source for this connection.
b. Select the existing Aws s3 destination as destination for this connection.
c. Select Sync mode either Replicate source or Append Historical changes.
d. Select Replication frequency as Every hour 
![image](https://github.com/user-attachments/assets/d22373d9-0409-4d37-9f48-592004b54126)
It will Sync your google sheet data to Aws S3 every 1 Hour without human intervention.
