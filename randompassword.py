#! /usr/bin/env python

import random, string

def rand_str():
	num = int(raw_input('Enter the numbers of password: '))
	length = int(raw_input('Enter the length of password: '))
	for i in range(num):
		chars = string.letters + string.digits + '@#$&*'
		s = [random.choice(chars) for i in range(length)]
		a = ''.join(s)
		print a

if __name__ == '__main__':
	rand_str()