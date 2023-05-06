from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pyautogui
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from docx import Document
from io import BytesIO
from googleapiclient.http import MediaIoBaseDownload
import io
import os

CLIENT_SECRETS_FILE = 'credentials.json'

# The scopes that the application requests access to
SCOPES = ['https://www.googleapis.com/auth/drive']

# Create a flow instance to handle the OAuth2 authorization process
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)

# Run the authorization flow and authorize the user
creds = flow.run_local_server(port=0)

# Use the authorized credentials to access the Google Drive API
drive_service = build('drive', 'v3', credentials=creds)
document_service = build('docs', 'v1', credentials=creds)
# Replace the placeholder with the name of the document you want to find
DOCUMENT_NAME = 'Demo'
NEW_FILE_NAME = '<New File Name>'

export_service = build('drive', 'v3', credentials=creds)

try:
    # Search for the document with the specified name
    query = "mimeType='application/vnd.google-apps.document' and trashed=false and name='{}'".format(DOCUMENT_NAME)
    response = drive_service.files().list(q=query).execute()
    files = response.get('files', [])

    # If the search returned any results, download the contents of the first matching document
    if files:
        document_id = files[0]['id']
        file_path = 'E:/pythonProject2/file.txt'
        print('Found document with ID: %s' % document_id)
        file_id = document_id

        # pylint: disable=maybe-no-member
        request = drive_service.files().export_media(fileId=file_id,
                                                     mimeType='text/plain')
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(F'Download {int(status.progress() * 100)}.')
#        if not os.access(file_path, os.W_OK):
#            print(f'Error: You do not have write permissions for {file_path}')
#            # change file path permissions
#            os.chmod(file_path, 0o777)  # set permissions to read, write, and execute for all users
#            print(f'Permissions for {file_path} have been changed to allow writing')
#        else:
#            print(f'You have write permissions for {file_path}')
        with open(file_path, 'wb') as f:
            f.write(file.getbuffer())
    else:
        print('Could not find document with name %s' % DOCUMENT_NAME)

except HttpError as error:
    print('An error occurred: %s' % error)
