#! /usr/bin/python
# https://www.anotherhome.net/1917

import os
import re

def get_files(path):
	filepath = os.listdir(path)
	files = []
	for fp in filepath:
		fppath = path + '/' + fp
		if (os.path.isfile(fppath)):
			files.append(fppath)
		elif(os.path.isdir(fppath)):
			files += get_files(fppath)
	return files

def get_important_word(files):
	worddict = {}
	for filename in files:
		f = open(filename,'rb')
		s = f.read()
		words = re.findall(r'[a-zA-Z0-9]',s)
		for word in words:
			worddict[word] = worddict[word] + 1 if word in worddict else 1
		f.close()
	wordsort = sorted(worddict.items(), key=lambda e:e[1], reverse = True)
	return wordsort

if __name__ == '__main__':
	files = get_files('/Users/fuhu/fuhu/tmp')
	print files
	wordsort = get_important_word(files)

	maxnum = 1
	for i in range(len(wordsort) - 1):
		if wordsort[i][1] == wordsort[i + 1][1]:
			maxnum += 1
		else:
			break
	for i in range(maxnum):
		print wordsort[i]