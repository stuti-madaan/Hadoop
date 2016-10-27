#!/usr/bin/python

# Reducer for session generation.
# Here we assemble user sessions

import sys
from operator import itemgetter


from collections import defaultdict

def read_key_value(file):
	for line in file:
        # split the line into components, before and after the tab
		yield line.strip().split('\t', 1)



def session_classify(event_list):
	k = [] 
	for i in range(0,len(event_list)):
		if event_list[i]['event_target'] == 'contact form':
			k.append("submitter") 
		elif event_list[i]['event_action'] == 'click':
			k.append("clicker")
		elif event_list[i]['event_action']=='show' or event_list[i]['event_action']=='display':
			k.append("shower")
		elif event_list[i]['event_action']=='visit':
			k.append("visitor")
		else:
			k.append("other")
	
	if "submitter" in k:
		return "submitter"
	elif "clicker" in k:
		return "clicker"
	elif "shower" in k:
		return "shower"
	elif "visitor" in k:
		return "visitor"
	elif "other" in k:
		return "other"
		
def main():
	current_user_id = None
	event_list = []
	car_list=[]
	user_id = None

	for user_id, event_string in read_key_value(sys.stdin):
        # eval() converts a data structure described on a string
        # into that internal data structure (for example, a dictionary).
		
		event = eval(event_string)
		event_details={}
		car={}
	
		for i in ("event_action","event_target","timestamp","vin"):
			event_details[i] = event[i]
		
		
		
		car[event["vin"]] = {"condition":event["condition"] ,"year":event["year"] ,"make":event["make"] ,  "model":event["model"] ,
			"price":event["price"] ,"mileage":event["mileage"] }
		
		# Assemble
		if user_id == current_user_id:
			if event_details not in event_list:
				event_list.append(event_details)
			if car not in car_list:
				car_list.append(car)
			continue
		else:
			if current_user_id:
				new_event_list = sorted(event_list, key=itemgetter('timestamp'))
				print '{}:{}\t{}\n{}'.format(current_user_id,session_classify(event_list),new_event_list,car_list)
			current_user_id = user_id
			event_list = [event_details]
			car_list=[car]
	
	if user_id == current_user_id:
		new_event_list = sorted(event_list, key=itemgetter('timestamp'))
		print '{}:{}\t{}\n{}'.format(current_user_id,session_classify(event_list),new_event_list,car_list)

		
		
if __name__ == "__main__":
	main()
