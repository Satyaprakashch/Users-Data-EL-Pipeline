# Documentation for the EL Pipeline Project Using FastAPI, Google Cloud Console, Airbyte and AWS S3

This documentation provides a comprehensive guide to setting up and running an Extract and Load (EL) Pipeline using FastAPI, Google Cloud console, Airbyte and AWS S3.

# Table of Contents
#### 1. Project Overview
#### 2. Prerequisites
#### 3. Google Cloud Project Setup
#### 4. Google Sheets API Setup
#### 5. Airbyte Setup and Configuration
#### 6. AWS S3 Configuration
#### 7. Project Structure
#### 8. Code Explanation
#### 9. Running the Project
#### 10. API Endpoint Details
#### 11. Error Handling and Troubleshooting

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
![image](https://github.com/user-attachments/assets/b4d29f42-3cca-4fff-bc33-18fcd7798967)
![image](https://github.com/user-attachments/assets/a386022d-89b7-4c81-b813-54cf913e09fd)

#### Enable Google Sheets APIs:
a. In the Google Cloud Console, navigate to APIs & Services > Library.<br>
b. Enable the Google Sheets API.<br>
