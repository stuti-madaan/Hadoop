#!/usr/bin/python

# Mapper for session generation.
# Here we examine event log entries

import sys

field_name_list = ['user_id', 'event', 'timestamp', 'vin', 'condition', 'year', 'make', 'model', 'price', 'mileage' ]

def read_input(file):
	for line in file:
        # split the line into individual fields (fields are delimited by tab).
		yield line.strip().split('\t') #returns a list# 

		
def digest_log_entry(field_value_list):
	field_value_dict = {}
	for i in range(len(field_name_list)):
		if i==1:
			field_value_dict['event_action'] = field_value_list[1].split()[0]
			field_value_dict['event_target'] = ' '.join(field_value_list[1].split()[1:])
		else:
			field_value_dict[field_name_list[i]] = field_value_list[i] ## position by position aligining ## 
	return field_value_dict

def main():
    # input comes from STDIN (standard input)
    # data is the generator that produces individual inputs
	
	data = read_input(sys.stdin)

    # For each log entry, digest all the fields,
    # output the user_id as the key,
    # output the digested log entry (a dictionary) as the value

	for log_entry in sorted(data):
		digested_log_entry = digest_log_entry(log_entry)
		print '%s\t%s'% ( digested_log_entry['user_id'], digested_log_entry)


if __name__ == "__main__":
	main()
