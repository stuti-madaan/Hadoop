#!/usr/bin/python

import sys

from collections import defaultdict

#-- Define a dictionary which can hold list-----
new_dict = defaultdict(list)

#-- For every line of Map output, remove spaces and split by a tab to separate out To/Bcc/Cc/From:EmailID & Message-ID components
for line in sys.stdin:
	line=line.strip()
	roll , message = line.split('\t',1)
	message = message.strip('[').strip(']').strip("'")

	#-- if the combination of Email ID and To/Bcc/Cc/From already exists in the dictionary, then append new message ID to the list--
	try:
	#-- Check if the message ID already exists : no duplicates
		if message not in new_dict[roll]:
			new_dict[roll].append(message)

#-- else create a new key for the new roll and update with the message ID--
	except:
		new_dict[roll]=[None]
		new_dict[roll][0]= message


#--- Print the results --
for roll in new_dict.keys():
	print '%s\t%s'% (roll, sorted(new_dict[roll])) #--- Printing with lexicographical sorting
