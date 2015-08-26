#! /usr/bin/python 

import os
import glob

def get_files(path):
	return glob.glob(path + r'/*')

def count_lines(files):
	line, blank, note = 0, 0, 0
	for filename in files:
		f = open(filename, 'rb')
		for l in f:
			l = l.strip()
			line += 1
			if l == '':
				blank += 1
			elif l[0] == '#' or l[0] == '/':
				note +=1
		f.close()
	return (line, blank, note)
if __name__ == '__main__':
	files = get_files('/Users/fuhu/fuhu/tmp')
	print files
	lines = count_lines(files)
	print 'line(s): %d, blank line(s): %d, note line(s): %d' %(lines[0], lines[1], lines[2])