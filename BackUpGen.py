import os
import time
#the files and directories which will be backed up
source = 'C:\\Users\\pcc\\Desktop\\IT BOOK'
#The back up must be stored in a main directory
target_dir = 'D:\\ICE'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)#make directory
#the files are backed up in zip file
#the current day is the name of the subdirectory
    
today = target_dir + os.sep + time.strftime('%Y%m%d')
#the current time is the name of the zip archive
now = time.strftime('%H%M%S')

#Take a comment from the user to create the name of the zip file
comment = input('Enter a comment -->')

#check if a comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'
    
#create the subdirectory if it is not already there
if not os.path.exists(today):
    os.mkdir(today)
    print ('Succesfully created directory', today)
#we use the zip command to put the files in a zip  archive
zip_command = 'zip -r {0} {1}'. format(target,' '.join(source))

#Run the back UP
print('zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
 print ('Successfuly backup to', target)
else:
    print ('Backup failed')
    
