
import os
import glob
import collections
import itertools
import sys
import re
import linecache


def bit_ops(num, bits_to_get_from_lsb):
    print('bits_to_get_from_lsb = ' + str(bits_to_get_from_lsb))
    local = 0xFF
    local = local << bits_to_get_from_lsb
    print(hex(local))
    bitmask = local & 0xFF
    bitmask = bitmask ^ 0xFF
    print('bitmask =' + str(hex(bitmask)))
    number = num
    print('Number is' + str(hex(number)))
    print('Passed num is' + str(hex(num)))
    var_value = number & bitmask
    print('Var value is' + str(hex(var_value)))
    print('Number has now become' + str(hex(number)))
    number = number >> bits_to_get_from_lsb
    print('the input byte is now ' + str(hex(number)))
    return (number, var_value)

byte_stream = '10 FC'
byte_string = byte_stream.replace(" ", "")
print('byte_string is ' + byte_string)
bytes = [byte_string[i:i+2] for i in range(0, len(byte_string), 2)]
count = 0
linecount = 0

for i in range(0, len(byte_string)):
    one_byte = bytes[i]
    print('first byte from left ' + str(one_byte))
    one_byte = int(one_byte, 16)
    print('first byte from left in hex' + str(hex(one_byte)))

    path = 'C:\\Python_programs'
    for infile in glob.glob( os.path.join(path, 'sample*') ):
        with open(infile) as f:
            if linecount != 0:
                    line = linecache.getline(infile, linecount)
                    print('Hit the linecount check')
                    print('The line now points to ' + line)
            for line in f:
                linecount = linecount + 1
                line1 = line.replace(" ", "")
                x = re.findall(r':(\w+)', str(line1))
                count = count + int(x[0])
                print('bits covered so far ' + str(hex(count)))
                new_num, var_value = bit_ops(one_byte, int(x[0]))
                one_byte = new_num
                if count == 8:
                    print('Exiting Line for loop, 8 bits covered')
                    print('Lines covered so far ' + str(linecount))
                    count = 0
                    break
                print(new_num, one_byte, var_value)







            
