from dropbox.files import WriteMode
import os
import dropbox


class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

            
        for root, dirs, files in os.walk(file_from):

            for filename in files:
#Making the local path
                local_path = os.path.join(root, filename)

#Making the Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
#Uploading the file to be transfered
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.Bidu21ZKrIwPYGtxBkHIOb1dqUKnUsQ9ybStWf8lJ64k9nV1-R83XF4ogvTLUdwnNL0vmAYJY9aD6TrtFDtKgmnRnY3aCZrT5jUYQZxIFZF7jI1VCrzTu7qTcRpdj1dom6I8cX8'
    transferData = TransferData(access_token)

    file_from = str(input("File to be uploaded: "))
    file_to = input("full path to upload the file to: ") 

    transferData.upload_file(file_from,file_to)
    print("File moved")

main()
