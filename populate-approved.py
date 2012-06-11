#!/usr/bin/env python
import sys

ODS_FIELDS = ['Timestamp',
 'Link to Qt DevNet profile',
 'Qt BugReports profile',
 'Full Name',
 'Affiliation',
 'Reasons for attending',
 'Invited by?',
 'Visa support?',
 'Travel sponsorship?',
 'T Shirt Size',
 'T Shirt Style',
 'Travel cost (estimate)',
 'Email address',
 'What coverage do you need?',
 'Nick',
 'Interests',
 'Country',
 'Arriving From',
 'Reason to be sponsored']



CSV_FIELDS = ['full-name',
 'nickname',
 'affiliation',
 'interests',
 'reasons-for-attending-1',
 'invited_by',
 'profile',
 'copy5_of_full-name',
 'travel-sponsorship',
 'country_type',
 'visa-support',
 't-shirt-size',
 't-shirt-style',
 'email',
 'dt']

# this takes ODS field index and converts it
# to CSV field index.
FIELD_DICT = {
	'Timestamp' : 14,
	'Link to Qt DevNet profile' : 6,
	'Qt BugReports profile' : 7,
	'Full Name': 0,
	'Affiliation' : 2,
	'Reasons for attending': 4,
	'Invited by?': 5,
	'Visa support?': 10,
	'Travel sponsorship?': 8,
	'T Shirt Size': 11,
	'T Shirt Style': 12,
	'Travel cost (estimate)': 'ignore',
	'Email address': 13,
	'What coverage do you need?': 'ignore',
	'Nick': 1,
	'Interests': 3,
	'Country': 9,
	'Arriving From': 'ignore',
	'Reasons to be sponsored': 'ignore',
	}

# created an inversed dict for the inverse lookup

INVDICT = dict((y,x) for x,y in FIELD_DICT.iteritems() if y!='ignore')

print INVDICT

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print 'usage: %s <approved.csv> <applied.csv>'
		sys.exit(1)
	approved = open(sys.argv[1], 'rb')
	applied  = open(sys.argv[2], 'rb')
	approved_dialect = csv.Sniffer().sniff(approved.read(1024))
	applied_dialect = csv.Sniffer().sniff(applied.read(1024))
	approved.seek(0)
	applied.seek(0)
	# build applied CSV data for lookup
	applied_reader = csv.reader(applied, applied_dialect)
	applied_header = applied_reader.next()
	applied_data = {}
	for l in applied_reader:
		applied_data[l[13]] = l
	# build approved data for iteration
	approved_reader = csv.reader(approved, approved_dialect)
	approved_header = approved_reader.next()
	approved_data = {}
	for l in approved_reader:
		approved_data[l[12]] = l
	# the real thing
	merged = {}
	for key in approved_reader:
		# key is email
		if key in applied_data:
			merged[key] = applied_data[key]
		else:
			# rearrange approved fields to match
			# applied_data 's columns.
			pass

		
		




	
		
		
