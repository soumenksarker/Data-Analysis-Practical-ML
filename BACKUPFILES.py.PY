import os
import time
#the files and directory are backed up specified in a list
source = ['''C:\\My documents''', 'C:\\Code']
#the backup must be stored in a main backup directory
target_dir = 'E:\\Backup'
#the files will be backed up in a zip file
#the name of the zip archive is the current date and time
target = target_dir + os.sep + \\time.strftime('%Y%M%D%H%M%S') + '.zip'

#creat target directory if it is not present
if not os.path.exists(target_dir):
   os.mkdir(target_dir)#make directory
#we use the zip command to put the file in a zip archive
zip_command = 'zip-r{0}{1}'.format(target,' '.join(source))
#run the backup
print('zip command is :')
print (zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print ('Backup FAILED')
