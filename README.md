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
  Google Cloud account
  AWS account with S3 access
  Airbyte instance for data synchronization
  FastAPI, Uvicorn, and other dependencies

### 3. Google Cloud Project Setup

