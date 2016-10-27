#!/usr/bin/python

import sys
import re
from collections import defaultdict

#--- get all lines from stdin ---
for line in sys.stdin:

#-- Define an empty dictionary-----
	d=defaultdict()
	
	#--- Split the messages by tab to extract To, From , Cc, Bcc features from the email
	elements = line.split('\t')
	
	#----for each feature in an email, separate "To","From","Cc","Bcc" an corresponding values of hese fields. 
	#-- Finally creating a dictionary where keys are To/From/Cc/Bcc and Values are the corresponding values of these fields in the email. 
	#-- Also, removing redundant characters using strip function
	
	for feature in elements:
		k=((feature.split(':')))
		if k[0] in ('Message-ID','From','To','Cc','Bcc'):
			d[k[0]]=re.findall(r'[\w\.-]+@[\w\.-]+', k[1])
			
			
	#--- Defining a blank dictionary for Map output format
	#---if the key is not Message-ID i.e. if Key is To, From, Cc or Bcc, then split the email-Ids separated by commas. 
	#--- For each of these email IDs paired up with To, From, Cc or Bcc, Assign the message ID in the values of the new dictionary k 
	
	k=defaultdict()
	for i in d.keys():
		if i != 'Message-ID' :
			for e in d[i]:
				k[i+':'+ e.lower()] = d['Message-ID']
	
	#--- Printing the final result as lines
	for feature in k.keys():
		print '%s\t%s' % (feature, k[feature])
