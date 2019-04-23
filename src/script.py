# This program creates a text document that can be uploaded to moodle server.
# By Wontez D Morgan wontez@protonmail.com 23 April 2019

from pathlib import Path 

# Creat code to get user input and display user interface


# Gets home directory and sets working directory to the users Desktop
path = Path.home()
desktop = path / 'Desktop'

# Creates file on users Desktop
uploadFile = desktop / 'newfile.txt'
Path(uploadFile).touch()

# Writes content to the file created on the users Desktop
Path(uploadFile).write_text('wontez morgan') 