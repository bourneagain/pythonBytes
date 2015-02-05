"""
/var/log/apache2/access_log 
"""
import re
def parse_log(log_name):
	regex='(^[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3})\s(.*?)\s(.*?)\s\[(.*?)\]\s\"(.*?)\"\s(.*?)\s(.*?)$'
	with open(log_name,'r') as fp:
		for lines in fp:
			if re.match(regex,lines):
				rematch=re.match(regex,lines).groups()
				print rematch
			




log_name='/var/log/apache2/access_log'
parse_log(log_name)