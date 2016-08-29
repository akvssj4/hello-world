#!/usr/bin/python

import sys
import datetime

#print 'Number of arguments:', len(sys.argv), 'arguments.'
log = str(sys.argv[1])
print 'Log:', log
print 'Current Time:', datetime.datetime.now()

# Open a file
fo = open("foo.txt", "a")
fo.write( str(datetime.datetime.now())+"\n"+log+"\n");

# Close opend file
fo.close()
