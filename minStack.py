class Stack():
	def __init__(self):
		self.astack = []
		self.bstack = []

	def min_(self):
		if not self.bstack:
			return 999999
		else:
			return self.bstack[-1]
	def push(self, data):
		if data < self.min_():
			self.bstack.append(data)
		self.astack.append(data)
	def pop(self):
		if not self.astack:
			return None
		a = self.astack.pop()
		if a == self.min_():
			self.bstack.pop()
		return a
	def getmin(self):
		return bstack[-1]

trystack = Stack()
trystack.push(1)
trystack.push(2)
trystack.push(-1)
trystack.push(5)
trystack.push(-3)
trystack.push(7)
print trystack.min_()
print trystack.pop()
print trystack.pop()
print trystack.pop()
print trystack.pop()
print trystack.pop()
print trystack.pop()
print trystack.pop()

print trystack.min_()



# # from bs4 import BeautifulSoup
# # f = open("/tmp/a html", "r")
# # soup = BeautifulSoup(f,from_encoding="utf-8")
# # a=soup get_text()
# # str(para) encode('utf-8')

# from bs4 import BeautifulSoup
# import re
# import codecs
# import sys
# # f = open('/tmp/a html')
# # html = f read()
# # soup = BeautifulSoup(html)
# # body = soup body contents
# # para = soup get_text() encode("utf-8")
# with open("/tmp/a.html", "r") as f:
#     soup = BeautifulSoup(f.read())

# # print soup.title.string
# print soup.body
# #  encode("utf-8")

# # from bs4 import UnicodeDammit
# # import lxml

# # def decode_html(html_string):
# #     converted = UnicodeDammit(html_string, isHTML=True)
# #     if not converted unicode:
# #         raise UnicodeDecodeError(
# #             "Failed to detect encoding, tried [%s]",
# #             ', ' join(converted triedEncodings))
# #     # print converted originalEncoding
# #     return converted unicode

# # root = lxml html fromstring(decode_html(tag_soup))


