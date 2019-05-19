#!/usr/bin/env python

import sys

def subsys_test(number,multiplier):
	"""
	Returns a number multiplied by the multiplier inputted by the user
	"""
	result = number * multiplier
	return result
	
def main():
	test1 = subsys_test(1,3)
	print ("Hello World!")
	print (test1)
	return test1
		
if __name__ == '__main__':
	main()