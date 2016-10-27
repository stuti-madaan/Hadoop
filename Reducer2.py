#!/usr/bin/python
import sys
from collections import defaultdict

word2count = defaultdict(list)
    
# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	
	line = line.strip()
	
	# parse the input we got from mapper
	word, msg, count, sos = line.split('\t', 3)
	
	# convert count, number of messages and squared count (currently a string) to int
	try:
		count = int(count)
		msg = int(msg)
		sos = int(sos)
	
	except ValueError:
        # Count was not a number
		continue
	try:
		# increment msg, count and squared sum for every word as the new line comes in
		word2count[word][0] = word2count[word][0] + msg
		word2count[word][1] = word2count[word][1] + count
		word2count[word][2] = word2count[word][2] + sos
		
		# updating the minimum number of times a word appears in a message
		if count< word2count[word][3]:
			word2count[word][3] = count
		else:
			word2count[word][3] = word2count[word][3]
	
		# updating the maximum number of times a word appears in a message
		if count>word2count[word][4]:
			word2count[word][4] = count
		else:
			word2count[word][4] = word2count[word][4]
		
		#Finding Mean 
		word2count[word][5] = round(word2count[word][1]/float(word2count[word][0]),2)
		
		#Finding Variance
		word2count[word][6] = round((word2count[word][2]/float(word2count[word][0])) - word2count[word][5] **2 ,2)
	
	except:
		# if the word appears for the first time, create an empty key-value pair
		word2count[word] = [None]*7
		word2count[word][0] = msg
		word2count[word][1] = count
		word2count[word][2] = sos
		
		#initialize min and maximum for a word seen for the first time
		word2count[word][3] = int(100)
		word2count[word][4] = int(1)
		
		#Update minimum
		if count<word2count[word][3]:
			word2count[word][3] = count
		else:
			word2count[word][3] = word2count[word][3]
		
		#update maximum
		if count>word2count[word][4]:
			word2count[word][4] = count
		else:
			word2count[word][4] = word2count[word][4]

		
		#Finding Mean if the word occurs just once
		word2count[word][5] = round(word2count[word][1]/float(word2count[word][0]),2)
		
		#Finding Variance if the word occurs just once
		word2count[word][6] = round((word2count[word][2]/float(word2count[word][0])) - word2count[word][5] **2 ,2)
	
for word in word2count.keys():
	print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s'% ( word, word2count[word][0],word2count[word][1],word2count[word][2],word2count[word][3],word2count[word][4],word2count[word][5],word2count[word][6] )
