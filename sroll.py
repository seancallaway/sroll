#!/usr/bin/python

import sys, getopt, random

def main(argv):
	rawdice = ''
	numdice = 0
	diesize = 0
	modifier = 0
	result = 0
	
	numargs = len(sys.argv)
	
	if numargs < 2 or numargs > 3:
		print 'Usage:  sroll.py #d# (+modifier)'
		sys.exit(2);
	elif numargs == 3:
		modifier = sys.argv[2]
	rawdice = sys.argv[1]
	
	random.seed()
	
	numdice, diesize = rawdice.split('d', 1)
	
	# Debugging bit to verify input
	#print 'Number of dice: ', numdice
	#print 'Die size: ', diesize
	#if modifier != 0:
	#	print 'Modifier: ', modifier
	
	try:	
		# Sanitize and form input
		numdice = int(numdice)
		diesize = int(diesize)
		modifier = int(modifier)
		
		output = 'Rolling ' + rawdice + ' plus ' + str(modifier) + ':  '
		
		# Roll the dice
		for i in range(numdice):
			rolled = random.randint(1, diesize)
			if i + 1 < numdice:
				output += '[' + str(rolled) + '] + '
			else:
				output += '[' + str(rolled) + ']'
			result += rolled
	
		# Add the modifier
		if modifier != 0:
			output += ' + ' + str(modifier)
			result += modifier
		
		print output, ' = ', str(result)
	except ValueError:
		print 'Usage:  sroll.py #d# (+modifier)'
	except:
		print 'Unexpected error!'
		raise


if __name__ == "__main__":
	main(sys.argv[1:])
