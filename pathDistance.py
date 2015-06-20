from geopy.distance import vincenty as dist
import sys
import os
import re
debug = False

def checklatlongline(line):
	if re.match("<gx:coord>", line):
		return True
	else:
		return False

def check(line):
	regex='^<gx:coord>(.*)</gx:coord>$'
	test = re.match(regex, line)
	lat = float(test.group(1).split(" ")[0])
	lon = float(test.group(1).split(" ")[1])
	return (lat, lon)


def calcPathDistance(filename):
	totDistance = 0
	f = open(filename, "r")
	line = f.read().splitlines()
	for i in xrange(len(line)):
		if checklatlongline(line[i]):
			A_lat_lon = check(line[i])
			if debug:
				print i, line[i]
			i+=1
			while not checklatlongline(line[i]) :
				i+=1
				if i >= len(line):
					print totDistance/1000,"km"
					sys.exit()
				

			B_lat_lon = check(line[i])
			if debug:
				print i, "second", line[i]
			totDistance+=dist(A_lat_lon, B_lat_lon).m
			if debug:
				print A_lat_lon, B_lat_lon," : ",
				print totDistance
		i+=1

	print totDistance
	# a = (41.49008, -71.312796)
	# b = (41.499498, -81.695391)
	# print(dist(a, b))
filename = sys.argv[1]
calcPathDistance(filename)