#!/usr/bin/env python

import sys


if __name__ == '__main__':
    if len(sys.argv)<3:
        print "usage: %s appendto newfiledata" % sys.argv[0]
        sys.exit(1)
    appendto = sys.argv[1]
    newfiledata = sys.argv[2]
    import csv
    origfile = open(appendto, "rb")
    dialect = csv.Sniffer().sniff(origfile.read(1024))
    origfile.seek(0)
    reader = csv.reader(origfile, dialect)
    hasnext = True
    origlines = []
    while (hasnext):
        try:
            origlines.append(reader.next())
        except:
            hasnext = False
    existing = {}
    header = ''
    for l in origlines:
        if l[13] == 'email':
            header = l
            print header
            continue
        existing[l[13]] = l
    origfile.close()
    appendtofile = open(appendto, "a")
    newfile = open(newfiledata , 'rb')
    dialect = csv.Sniffer().sniff(newfile.read(1024))
    newfile.seek(0)
    reader = csv.reader(newfile, dialect)
    newcontent = []
    hasnext = False
    while (hasnext):
        try:
            newcontent.append(reader.next())
        except:
            hasnext = False
    for nl in newcontent:
        if nl[13] == 'email': continue
        existing[nl[13]] = nl
    ofile = open("ouput-%s" % appendto, 'wb')
    writer = csv.writer(ofile, dialect=dialect)
    writer.writerow(header)
    for i in existing:
    #    print "KEY = %s:\n" % i 
    #    print existing[i]
    #    print "---"
        writer.writerow(existing[i])
    ofile.close()


    
    



        

    
