# This program creates a text document that can be uploaded to moodle server.
# By Wontez D Morgan wontez@protonmail.com 23 April 2019

from pathlib import Path 

# Creat code to get user input and display user interface
rosterNumber = input("What is the class number?: ")
rosterYear = input("What is the class year? ")
rosterName = rosterNumber + "-" + rosterYear
createFilename = rosterName + ".txt"

# Template for input
lineOne = "username,password,firstname,lastname,email,course1,group1,type1"
lineStudents = rosterNumber + "-stu1,Student1,Student 1,Class " + rosterName + ",1Student" + rosterName + "@cc.mil,Common Core,Class " + rosterName + ",1"
lineInstructor = rosterNumber +"-inst,###password###,Instructor " + rosterNumber + ",Class " + rosterName + ",Instructor" + rosterName + "@cc.mil,Common Core,Class " + rosterName + ",2"


# Gets home directory and sets working directory to the users Desktop
path = Path.home()
desktop = path / 'Desktop'

# Creates file on users Desktop
uploadFile = desktop / createFilename 
Path(uploadFile).touch()

# Writes content to the file created on the users Desktop
Path(uploadFile).write_text('wontez morgan') 
Path(uploadFile).write_text('will this append') # didn't append  