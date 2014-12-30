import os
import sys
import subprocess

def list_dir(dirname):
	""" 
	Different ways of listing all the files under a given directory recursively
	"""
	res=[]
	if not os.path.isdir(dirname):
		print "error"
		sys.exit(1)
	for dirpath, dirn, filename in os.walk(dirname):
		if filename: 
			res.extend(filename)
	command="ls -R "+dirname+" | grep '/'"
	command2="find "+dirname+" -type f"
	p=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
	p2=subprocess.Popen(command2,shell=True,stdout=subprocess.PIPE)


	print "---------------------------------"
	print "USING os.walk moduel", res
	print "---"
	print "USING ls -R command", p.stdout.readlines()
	print "---"
	print "USING find <dir> command" ,p2.stdout.readlines()

list_dir('/tmp/TEST')
