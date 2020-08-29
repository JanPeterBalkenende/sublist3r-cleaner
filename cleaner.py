#!/bin/python3

import sys

path = input("What is the path to your sublist3r output file?\n")

delete = ["[92m","[0m"]

datalog = []
#with open("%s" % (path)) as list:
#	lines = list.read().split("\n")


f = open("%s" % (path), "r")	
for line in f:
	for word in delete:
		if word in line:
			line = line.replace(word,"")
		datalog.append(line)
f.close()
f = open("%s" % (path), "w")
for line in datalog:
	f.write(line)
f.close()
	
