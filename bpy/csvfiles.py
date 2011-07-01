'''
Created on Jun 23, 2010

@author: brent
'''

import csv
spamReader = csv.reader(open('eggs.csv'), delimiter=' ', quotechar='|')
for row in spamReader:
    print ', '.join(row)

### READ Reporting errors
import csv, sys
filename = "some.csv"
reader = csv.reader(open(filename, "rb"))
try:
    for row in reader:
        print row
except csv.Error, e:
    sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))


spamWriter = csv.writer(open('eggs.csv', 'w'), delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
spamWriter.writerow(['Spam'] * 5 + ['Baked Beans'])
spamWriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
