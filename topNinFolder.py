import sys
import glob
import os
import subprocess
from collections import defaultdict,Counter
#import Counter

def topn(dir):
	file_list=[]
	# for file_name,dir_name,path_nath in os.walk(dir):
	# 	print path_nath
	top=defaultdict(lambda :0)
	cmd="find "+dir+" -type f"
	p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
	for file in p.stdout.readlines():
		print "FILE :",file
		with open(file.strip(),"r") as f:
			for line in f:
				for word in line.split(' '):
					if len(word) > 3 and not word.isdigit() and word.find('\\') == -1 :
						top[word]+=1
	return sorted(top.items(),key=lambda x: x[1])[-1:-11:-1]



	#return len(file_list)
print topn(sys.argv[1])
