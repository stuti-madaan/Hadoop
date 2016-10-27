#!/usr/bin/python

import sys
from collections import defaultdict


#--- get all lines from stdin ---
for line in sys.stdin:
	d=defaultdict(list)
	#---Convert everything to lowercase--
	line = line.lower()
	#--- remove leading and trailing whitespace---
	line = line.strip()
	
	#--- split the line into words ---
	words = line.split()
	#--- For every word, checking if it exists in the dictionary already or not 
	#--- If it exists, Adding 1 to the count of words
	#--- AND squaring the above to get a square of count for each message
	
	for word in words:
		if word in d.keys():
			d[word][1] = d[word][1] + 1
			d[word][2] = d[word][1] ** 2 
	#--- if the word doesn't exist, create a new key-value for it in the dictionary
	#--- initialize the new key-value pair with value as list 
	#--- number of message= 1 for all words while processing one message at a time
	#--- count =1 and square as the square of count
		else:
			d[word] = [None]*3
			d[word][0] = 1
			d[word][1] = 1
			d[word][2] = d[word][1] ** 2
	
	#--- output tuples [word, message, word_count] in tab-delimited format---
	for word in d.keys():
		# For each word in the line, output a key/value pair
        # with the word as the key, and "1" as the value of message count, word_count and squared word count.
		print '%s\t%s\t%s\t%s' % (word, d[word][0],d[word][1],d[word][2])
