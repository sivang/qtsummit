#!/usr/bin/env python

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
	'Qt BugReports profile' : 'ignore',
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


if __name__ == '__main__':
	if len(sys.argv) < 3:
		print 'usage: %s <odsfile.csv> <csvfile.csv>'
		sys.exit(1)
	odsfile = open(sys.argv[1], 'rb')
	csvfile = open(sys.argv[2], 'rb')
	odsdialect = csv.Sniffer().sniff(odsfile.read(1024))
	csvdialect = csv.Sniffer().sniff(csvfile.read(1024))
	odsfile.seek(0)
	csvfile.seek(0)
	# build CSV data for lookup
	csvreader = csv.reader(csvfile, csvdialect)
	csvheader = csvreader.next()
	cvsdata = {}
	for l in csvreader:
		cvsdata[l[13]] = l
	# build ODS data for iteration
	odsreader = csv.reader(odsfile, odsdialect)
	odsheader = odsreader.next()
	odsdata = {}
	for l in odsreader:
		odsdata[l[
		




	
		
		
