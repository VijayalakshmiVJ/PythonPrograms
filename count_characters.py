
import subprocess
import os
import glob
import collections
import itertools
import sys
import re

path = 'C:\\Python_programs'
for infile in glob.glob( os.path.join(path, 'RCS_BXSX*') ):
    with open(infile) as f:
        before = collections.deque(maxlen=20)
        sys.stdout = open( str(pac_name) + '_extract.txt', 'w')
        for line in f:
            if search_string in line:
                if addr_pattern.search(line):
                    sys.stdout.writelines(before)
                sys.stdout.writelines(before)
                sys.stdout.write(line)
                sys.stdout.writelines(itertools.islice(f, 15))
                count = count + 1
            before.append(line)
        if count == 0:
                print('I am sorry, couldnn of PAC')

#print(lineno)
#print(words)
#print(characters)

