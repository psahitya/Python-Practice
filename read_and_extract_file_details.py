import os
import glob
import re
import sys
import string

path = ‘../sql-dir/’
prefix= ‘SAW_SRC_PATH’

for infile in glob.glob{ os.path.join(path, ‘q*.sql’)):
f = open(infile,’r’)
line = f.readline()
prefix_pos = string.find(line,prefix)

print infile+’ ‘+line(prefix_pos:)
f.closed