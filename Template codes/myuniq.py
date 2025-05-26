#!/usr/bin/env python3
import sys
numberOfArgs = len(sys.argv)
# Check if the number of args are correct
if numberOfArgs != 2:
    sys.stderr.write('Usage: %s inputFile\n' % sys.argv[0])
    sys.exit(1)
try:
    fh = open(sys.argv[1], 'r')
except:
    # A problem happened trying to open the file
    sys.stderr.write('cannot open input file %s\n' % sys.argv[1])
    sys.exit(2)
previousLine = '' # initialize
# implementing uniq utility
for line in fh.readlines():
    if line != previousLine: # filter
        print(line, end='')
    previousLine = line # update previous
fh.close()