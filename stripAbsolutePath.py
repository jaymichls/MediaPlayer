#!/usr/bin/python
# -*- coding: utf-8 -*-

f = open('Movies.list')

fm = open('Movies1.list', 'w')

wholeFile = f.read()

lines = wholeFile.split('\n')

for line in lines:
	
	size = len(line) - 1
	
	line = line[11:size-1]
	
	fm.write(line+'\n')

f.close()

fm.close()

