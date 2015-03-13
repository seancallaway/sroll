#!/usr/bin/python

import sys, getopt, random

def main(argv):
	rawdice = ''
	numdice = 0
	diesize = 0
	modifier = 0
	result = 0
	
	numargs = len(sys.argv)
	
	if numargs < 2:
		print 'Usage:  sroll.py #d# (+modifier)'
		sys.exit(2);
	elif numargs == 3:
		modifier = sys.argv[2]
	rawdice = sys.argv[1]
	
	random.seed()
	
	#############################
	# TODO: Sanitize user input #
	#############################
	
	numdice, diesize = rawdice.split('d', 1)
	
	# Debugging bit to verify input
	#print 'Number of dice: ', numdice
	#print 'Die size: ', diesize
	#if modifier != 0:
	#	print 'Modifier: ', modifier
		
	# Roll the dice
	for i in range(int(numdice)):
		rolled = random.randint(1, int(diesize))
		result += rolled
	
	result += int(modifier)
	
	print "Rolling", rawdice, "plus", modifier, ": ", result

if __name__ == "__main__":
	main(sys.argv[1:])
