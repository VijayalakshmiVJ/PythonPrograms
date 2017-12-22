
# Execute command line commands to extract (specified) history files from Sofia 
# and perform input string search and output only those history info matching string

import subprocess
import os
import glob
import collections
import itertools
import sys
import re

print('Enter the PAC name EG : RCS_BXSX')
pac_name = input()

print('Enter the FROM PAC version EG : 31.29-0')
from_pac = input()

print('Enter the TO PAC version EG : 30.23-0')
to_pac = input()

print('Enter the search string EG : OSC or SmartBCCH')
search_string = input()

#This command could have multiple commands separated by a new line \n
#strCommandLine = 'slist -hist -from_version 31.29-0 -to_version 30.23-0 RCS_BXSX'
print('Processing....please note the farther the FROM and TO PACs are, the longer the process takes.')

# Need to have PAC number as input as well
string = 'slist -hist -from_version ' + str(from_pac) + ' -to_version ' + str(to_pac) + ' ' + str(pac_name)

strCommandLine = string
file = open(str(pac_name) + '.txt', 'w')
ret = subprocess.call(strCommandLine, stdout=file)
count = 0

addr_pattern = re.compile(
    r'- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -',
    flags=re.IGNORECASE
)

if ret == 0:
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
                print('I am sorry, couldnt find the string you entered in the given PACs. You could try again by changing from and to version of PAC')

else:
    print('Failed to download History/Pac files from Sofia. Check if the PAC version is entered correctly or for connectivity issues!')
    
