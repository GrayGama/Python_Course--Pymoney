#!/usr/bin/env python3
import sys
numberOfArgs = len(sys.argv)
if numberOfArgs < 2:
    sys.stderr.write('Usage: %s inputFiles\n' % sys.argv[0])
    sys.exit(1)

for fileName in sys.argv[1:]:
    try:
        fh = open(fileName, 'r')
    except:
        sys.stderr.write('cannot open input file %s\n' % fileName)
        sys.exit(2)

    for line in fh.readlines():
        print(line, end='')
    fh.close()