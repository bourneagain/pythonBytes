import sys
PWD="/Users/sam/cs410/TEAM_BHP_DATA_TOPARSE/srajend2_txt/"
OUTFILE=PWD+"../JSON_OUTPUT.json"
def read_list_files():
	f_name, input_file = sys.argv
	#input_file="/tmp/a.txt"
	of = open(OUTFILE, 'w')

	with open(input_file) as f:
		for txt_file in f:
			op=[]
			txt_file = txt_file.strip()
			lines = open(PWD+txt_file).read().splitlines()
	#		create_json(txt_file.strip())
			str1 = r'{ "create": { "_index": "srajend2_index", "_type": "doc"}}'
			op.append(str1)
			op.append("\n")
			doc_id = txt_file
			print ""
			print lines
			print ""
			try:
				url = lines[0].strip()
				title = lines[1].strip()
			except:
				continue

			str1 = "{\"doc_id\": \""+txt_file+"\",  \"url\" : \""+url+"\", \"title\" : \""+title+"\", \"body\" : \""+''.join(lines[2:])+"\"}"
			op.append(str1)
			op.append("\n")
			of.write(''.join(op))

read_list_files()

# def create_json(in_file):
	# since small read entire file in array




read_list_files()
	#  	{ "create": { "_index": "netID_index", "_type": "doc"}}
  	# 	{"doc_id": "NAME_OF_TXT_FILE",  "url" : "YOUR_URL", "title" : "YOUR_TITLE", "body" : "YOUR


		
