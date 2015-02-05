import subprocess

def printme(process_name):
	command = "ps -o'pid,ppid,command' | grep "+process_name
	op=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
	for line in op.stdout.readlines():
		print line
		#for word in line.split():
			

printme('python')

# import sys,subprocess,os,pprint

# def print_process_info(process_name):
# 	"""
# 	Program to print process information in a friendly manner
# 	@var1 : process_name
# 	"""
# 	command = "ps -aef | grep "+process_name
# 	processOpen = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell = True)
# 	while True:
# 		line = processOpen.stdout.readline()
# 		#line = processOpen.stderr.readline()
# 		print "LINE:" + line
# 		if line == '':
# 			break

# #	stdout_list = stdout.decode('ascii').splitlines()
# #	pprint.pprint(stdout_list)

# print_process_info('python')

