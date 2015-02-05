import os,sys,glob,subprocess
def find_file(file_name):
	output=subprocess.Popen("find . -name "+file_name ,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
	print type(output)
	for i in output:
		print i
		print "-"
find_file('*.csv')
