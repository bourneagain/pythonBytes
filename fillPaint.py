import Queue
import time
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def getxy(self):
		return self.x,self.y
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	def __hash__(self):
		return hash(self.x+self.y)
def fillPaint(start):
	m = [
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', 'X', 'X', 'X', '_', '_', 'X', 'X', 'X', '_'],
    ['_', 'X', '_', 'X', 'X', 'X', 'X', '_', 'X', '_'],
    ['_', 'X', '_', '_', '_', '_', '_', '_', 'X', '_'],
    ['_', 'X', '_', '_', '_', '_', '_', '_', 'X', '_'],
    ['_', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '_'],
	['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]
	c = len(m[0])
	r = len(m)
	
	for i in range(r):
		for j in range(c):
			print m[i][j],
		print ""
	# print r,c
	visited = {}
	visited[start] = True
	q=Queue.Queue()
	q.put(start)
	markPoints = []
	while not q.empty():
		newpoint = q.get()
		x,y = newpoint.getxy()
		# print "EXPLORING FOR ", x,y
		# print ""
		explore=[]
		explore.append(Point(x,y+1))
		explore.append(Point(x+1,y))
		explore.append(Point(x-1,y))
		explore.append(Point(x,y-1))
		for points in explore:
			x,y = points.getxy()
			# print x,y
			if x>=0 and y>=0 and x<r and y<c and m[x][y] == '_' and (points not in visited):
				visited[points] = True
				markPoints.append(points)
				# print "ADDED ", x,y
				q.put(points)
		# print "-----------------------------------------------------------EXPLORE DONE for ",x,y
		# time.sleep(1)
	for i in markPoints:
		x,y = i.getxy()
		m[x][y] = "$" 
	print "AFTER"
	for i in range(r):
		for j in range(c):
			print m[i][j],
		print ""

start = Point(0,0) 
fillPaint(start)
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
# with open("/tmp/a html", "r") as f:
#     soup = BeautifulSoup(f read())

# print soup title string
# print soup get_text()
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


