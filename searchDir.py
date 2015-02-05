import os,sys,glob
def search(search_dir,search_text):
		if not os.path.isdir(search_dir):
			print "not a directory"
			sys.exit(1)
		else:
			os.chdir(search_dir)
#			for root, dirnames, filenames in os.walk(search_text):	
#				print root,dirnames,filenames
			for i in glob.iglob(search_text):
				print i
		

search('/Users/sam/pythonBytes/testing','*.csv')
