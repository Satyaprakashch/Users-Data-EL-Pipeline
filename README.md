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
#### 10. Error Handling and Troubleshooting
#### 11. Airbyte Setup and Configuration

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
The main components of the code are as follows:
### Imports: 
The necessary libraries are imported, including FastAPI, Google authentication libraries, and Pydantic for data validation.
##### SCOPES: Define scopes required for accessing Google Sheets and user information.
##### FastAPI Instance: An instance of FastAPI is created.
##### get_service() Function: This function handles authentication and returns a service object to interact with Google Sheets API.
##### list_spreadsheets Endpoint: This endpoint retrieves data from a user's spreadsheet and appends it to a predefined spreadsheet.



