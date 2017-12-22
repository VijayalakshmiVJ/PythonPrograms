
import os
import glob
import collections
import itertools
import sys
import re

addr_pattern = re.compile(
    r'- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -',
    flags=re.IGNORECASE
)

path = 'C:\Python_programs'
find = "-"
string = 'pdm'
string.lower()

string.upper()

for infile in glob.glob( os.path.join(path, 'IGWMNDSE*') ):
    print ('current file is: ' + infile)
    with open(infile) as f:
        sys.stdout = open( 'IGWMNDSE_extract.txt', 'w')
        before = collections.deque(maxlen=30)
        for line in f:
            if string in line:
                if addr_pattern.search(line):
                    sys.stdout.writelines(before) 
                sys.stdout.write(line)
                sys.stdout.writelines(itertools.islice(f, 30))
            before.append(line)
        
        

