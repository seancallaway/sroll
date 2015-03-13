#!/usr/bin/python

import sys, getopt

def main(argv):
	rawdice = ''
	numdice = 0
	diesize = 0
	modifier = 0
	
	numargs = len(sys.argv)
	
	if numargs < 2:
		print 'Usage:  sroll.py #d# (+modifier)'
		sys.exit(2);
	elif numargs == 3:
		modifier = sys.argv[2]
	rawdice = sys.argv[1]
	
	numdice, diesize = rawdice.split('d', 1)
	
	print 'Number of dice: ', numdice
	print 'Die size: ', diesize
	if modifier != 0:
		print 'Modified: ', modifier

if __name__ == "__main__":
	main(sys.argv[1:])
