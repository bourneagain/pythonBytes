def uglyNumbers(n):
	#print nth ugly number
	#http://www.geeksforgeeks.org/ugly-numbers/
	ulist= [-1]*n;
	ulist[0]=1
	q2=0
	q3=0
	q5=0
	nq2=2
	nq3=3
	nq5=5
	for i in range(1,n):
		minq = min(nq5,nq3,nq2)
		ulist[i] = minq
		if minq == nq2:
			q2+=1
			nq2=ulist[q2]*2
		elif minq == nq3:
			q3+=1
			nq3=ulist[q3]*3
		elif minq == nq5:
			q5+=1
			nq5=ulist[q5]*5
		# print nq2,nq3,nq5 ,"|",q2,q3,q5
	print ulist
	print minq
uglyNumbers(150)

# # from bs4 import BeautifulSoup
# # f = open("/tmp/a.html", "r")
# # soup = BeautifulSoup(f,from_encoding="utf-8")
# # a=soup.get_text()
# # str(para).encode('utf-8')

# from bs4 import BeautifulSoup
# import re
# import codecs
# import sys
# # f = open('/tmp/a.html')
# # html = f.read()
# # soup = BeautifulSoup(html)
# # body = soup.body.contents
# # para = soup.get_text().encode("utf-8")
# with open("/tmp/a.html", "r") as f:
#     soup = BeautifulSoup(f.read())

# print soup.title.string
# print soup.get_text()
# # .encode("utf-8")

# # from bs4 import UnicodeDammit
# # import lxml

# # def decode_html(html_string):
# #     converted = UnicodeDammit(html_string, isHTML=True)
# #     if not converted.unicode:
# #         raise UnicodeDecodeError(
# #             "Failed to detect encoding, tried [%s]",
# #             ', '.join(converted.triedEncodings))
# #     # print converted.originalEncoding
# #     return converted.unicode

# # root = lxml.html.fromstring(decode_html(tag_soup))


