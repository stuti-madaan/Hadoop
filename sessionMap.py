#!/usr/bin/python

# Read session

import sys

def main():
	## Read a line ##
	for line in sys.stdin:    
		## try to split the line by tab and output the three elements. If it's the "dataSet5sessions.tsv" file, this will run 
		try:
			user_id_string, event_list_string, vin_dict_string = line.strip().split('\t')
			# empty dictionary to save the output
			output_dict1={}
			
			# separate user id and session type
			user_id, session_type = user_id_string.split(':')
			
			# convert the event list back to list of dictionaries
			event_list = eval(event_list_string)
			
			# convert vin_dict back to dictionary 
			vin_dict = eval(vin_dict_string)
			
			# for every VIN in the dictionary, session = 1, 
			# for every VIN, count the number of corresponding events with event_action = "click"
			# for every VIN, contact form flag = 1 if any of the event_target = contact form
			for v in vin_dict:

				count_click= 0 
				contact_form_flag = 0 
				for e in event_list:
					if v==e['vin'] and e['event_action'] =="click" :
						count_click+=1 
					else:
						count_click = count_click
					if v==e['vin'] and e['event_target'] == "contact form" :
						contact_form_flag = max(contact_form_flag,1)
					else: 
						contact_form_flag = contact_form_flag
				
				#	Save the list as a value in the output dictionary for key = VIN 
				#	last two elements of the list being left = 0 for the impressions file
				output_dict1[v] = [1,count_click, contact_form_flag,0,0]
				
			# print tab separated results
				print '{}\t{}'.format(v, output_dict1[v])
		
		# if line is not tab separable, it gets separated by comma for the file "dataSet5imps.csv "
		except:
			vin, impression_type, impression_count = line.strip().split(',')
			output_dict2={}		
			
			# for SRP, input the impression count
			if impression_type == "SRP":
				output_dict2[vin] = [0,0,0,impression_count,0]
				
			# for VDP, input the impression count
			elif impression_type=="VDP":
				output_dict2[vin]= [0,0,0,0,impression_count]
			
			# print tab separated results
			print '{}\t{}'.format(vin, output_dict2[vin])


if __name__ == "__main__":
    main()
