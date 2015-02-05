# os.getcwd()
# os.chdir()
# os.system('syscall') 
# glob.glob(os.getcwd()+'/*.py')
import subprocess
import os
import glob 
import zipfile
def filep():
	# go to specific path 
	os.chdir('/Users/sam/Scripts/Scripts')
	print "PWD:",os.getcwd()

	#grab all csv files in there
	csv_files_list=glob.glob(os.getcwd()+'/*.csv')

	#print all files in the csv_files_list 
	for file in csv_files_list:
		print file

	#zip all csv files in the csv_files_list
	zip_name='myCSVs.zip'
	zf=zipfile.ZipFile(zip_name,"w")

	for file in csv_files_list:
		zf.write(file)

	#print zip information
	print zf.printdir()

	# get info of a specific member
	print zf.getinfo('Users/sam/Scripts/Scripts/abcd_checkList.csv')

	#extract the zip info /tmp/
	zf.extractall('/tmp/')

	zf.close()

	os.system('rm -rf /tmp/Users')
	os.system('rm /Users/sam/Scripts/Scripts/myCSVs.zip')
	print "FILES REMOVED"


def subp():
	"""
	examples of subprocess usage
	"""

	# list all open ports on server
	
filep()



