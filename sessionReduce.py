#!/usr/bin/python

# Read session

import sys

from collections import defaultdict

output_dict = defaultdict(list)

# function to read output of the mapper and splitting by tab
def read_key_value(file):
	for line in file:
        # split the line into components, before and after the tab
		yield line.strip().split('\t', 1)

		
def main():
	
	#separating out Key(VIN)-value and converting the value to list
	for vin, output_string in read_key_value(sys.stdin):
		output_list = eval(output_string)
        # eval() converts a data structure described on a string
        # into that internal data structure (for example, a dictionary).
		
		
		# Assemble
		
		# if the VIN already exists as a key in the output dictionary, then add elements 1,2,3,4,5 of the new line to the entry in dictionary
		try:
			output_dict[vin][0] += int(output_list[0])
			output_dict[vin][1] += int(output_list[1])
			output_dict[vin][2] += int(output_list[2])
			output_dict[vin][3] += int(output_list[3])
			output_dict[vin][4] += int(output_list[4])
		
		# if the VIN doesn't exist, create a new entry in the dictionary and enter values for 1,2,3,4,5 elements
		except:
			output_dict[vin] = [None]*5
			output_dict[vin][0] = int(output_list[0])
			output_dict[vin][1] = int(output_list[1])
			output_dict[vin][2] = int(output_list[2])
			output_dict[vin][3] = int(output_list[3])
			output_dict[vin][4] = int(output_list[4])
	
	# for every key in the dictionary, if the first three elements of the list are > zero, then print items
	# this operation performs the left join by printing out only the VINs which are present in the dataSet5sessions.tsv file.
	for k in sorted(output_dict):
		if (output_dict[k][0] + output_dict[k][1] + output_dict[k][2])> 0:
			print '{}\t{}'.format(k,output_dict[k])
			
		
		
if __name__ == "__main__":
	main()
