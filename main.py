from time import sleep
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaIoBaseDownload
import io
import os
import asyncio
from googleapiclient.http import MediaIoBaseUpload

def message_to_gdrive():
    while True:
        Message=input("Enter Your Text ! Type 'exit' For Exit:")
        if Message == "exit":
            exit()
        path_ = os.path.join(r"chats.txt") #path used
        chat_file = open(path_,'w')
        chat_file.write(Message)
        chat_file.close()

        with open( os.path.join(r"chats.txt") , 'r') as f:
            source_content = f.read()


        credentials = Credentials(
        token="ya29.a0AXooCgvrcAJwRdbXfbZSSCI9Ti071peOsC8bqdKfxiVwgnNroYVJsQjbHNxEkouvIJffp14RFlVWQJB02G5U7n6S1eow7b1fcDLAtdm3fUquwpba0YYwdMDiVNcWeRRzjB_0nDwCOp1usIpEjcD2-s0LsyIw-awaCgYKAWYSARISFQHGX2Mi4hKgRhyuM5WolDLvp9Mhig0171",
        refresh_token="1//0gVBr53npZiCYCRAAGBASNwF-L9IrlvWpcX_uR789oBOuzBa9OuKj-G7wmgDUX1IEJGNQq31LkwVK9m04kE5QWalWd2BX9xg",
        token_uri="https://oauth2.googis.com/token",
        client_id="515444003927-0fc6t835bkj9h6vr8d5ct0eh59i.apps.googleusercontent.com",
        client_secret="GOCSPX-06vTOt_FMcaQ9CqioqXdYU8F"
        )
        
        service = build('drive', 'v3', credentials=credentials)

        request = service.files().get_media(fileId= r"1QrlAxX6XLFKa9IU8E0HbK1j3Ik66XxZn")
        existing_content = request.execute().decode('utf-8')

        # Append and update destination file
        updated_content = source_content
        media_body = MediaIoBaseUpload(io.BytesIO(updated_content.encode('utf-8')), mimetype='text/plain')
        updated_file = service.files().update(
            fileId= r"1QrlAxX6XLFKa9IU8E0HbK1j3Ik66XxZn",
            media_body=media_body
        ).execute()

        #print(f'File ID: {updated_file.get("id")}') 
        
        sleep(1) # use async

def gdrive_to_message():
    temp=""
    file_content="None"
    while True: 

        path_ = os.path.join(r"chats.txt") #path used

        chat_file = open( path_ ,'r') #path used
        
        chat_file.read()

        # Path to your token file
        token_path = os.path.join(r"token.json")

        # Load the credentials
        creds = Credentials.from_authorized_user_file(token_path)
        
        service = build('drive', 'v3', credentials=creds)

        # Replace with the actual ID of your text file in Google Drive
        file_id = r'1QrlAxX6XLFKa9IU8E0HbK1j3Ik66XxZn'

        # Get the file content
        request = service.files().get_media(fileId=file_id)
        
        fh = io.BytesIO()
        
        downloader = MediaIoBaseDownload(fh, request)
        
        done = False
        
        while done is False:
        
            status, done = downloader.next_chunk()

        # Decode and print the content (assuming it's UTF-8 encoded)
        
        file_content = fh.getvalue().decode('utf-8')
        
        sleep(1)

        
        if temp != file_content:
            print(f"text --> {file_content}\n")
            temp = file_content

async def main():
    task = await asyncio.create_task(message_to_gdrive())
    await gdrive_to_message()
    
if __name__ == "__main__":
    os.system("cls")
    # call to main
    message_to_gdrive()
