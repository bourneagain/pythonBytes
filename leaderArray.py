def leader(a):
	max_ = a[len(a)-1]
	print max_
	for i in range(len(a)-2,-1,-1):
		if a[i] > max_:
			print a[i]
			max_ = a[i]

leader([13,17,5,4,6,2])

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


