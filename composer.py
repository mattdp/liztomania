#!/usr/bin/env python3

import csv
import sys, getopt

def emacsify(rows):
	output_text = ''

	for row in rows:
		output_text += f'* {row["name"]}\n'
		if row["detail"] != '':
			output_text += f'{row["detail"]}\n'

	return output_text

def parse_cli(argv):

	help_string = './composer.py\n-p <priority: ["red"|"yellow"|"green"]>\n-d <daytype: ["workday"|"weekend"]>'
	arguments = {}

	try:
		opts, args = getopt.getopt(argv,'hp:d:',['priority=','day_type='])
	except getopt.GetoptError:
		print(help_string)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print(help_string)
			sys.exit()
		elif opt in ("-p", "--priority"):
			arguments["priority"] = arg
		elif opt in ("-d", "--daytype"):
			arguments["day_type"] = arg
	
	return arguments

def main(argv):

	arguments = parse_cli(argv)

	csv_reader = ''
	selected_rows = []

	with open('./elements.csv') as csv_file:
		csv_reader = csv.DictReader(csv_file, delimiter=',')
		for row in csv_reader:
			selected_rows.append(row)

	formatted_output = emacsify(selected_rows)
	print(formatted_output)

	with open('./todays_routine.org', 'w') as file:
		file.write(formatted_output)

# needed to actually run the program
main(sys.argv[1:])