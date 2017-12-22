
# Loop through txt files and perform string search

import os
import glob
import collections
import itertools
import sys

path = 'D:\\userdata\\vijs\\Desktop'

for infile in glob.glob( os.path.join(path, 'RCS_BXSX*') ):
    print ('current file is: ' + infile)
    with open(infile) as f:
        before = collections.deque(maxlen=20)
        for line in f:
            if 'OSC' in line:
                sys.stdout.writelines(before)
                sys.stdout.write(line)
                sys.stdout.writelines(itertools.islice(f, 15))
                break  
            before.append(line)
        
        
    
    
    





        
    
