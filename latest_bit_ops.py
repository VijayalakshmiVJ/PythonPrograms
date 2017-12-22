import os
import glob
import collections
import itertools
import sys
import re
import linecache


def bit_ops(num, bits_to_get_from_lsb):
    #print('bits_to_get_from_lsb = ' + str(bits_to_get_from_lsb))
    local = 0xFF
    local = local << bits_to_get_from_lsb
    #print(hex(local))
    bitmask = local & 0xFF
    bitmask = bitmask ^ 0xFF
    #print('bitmask =' + str(hex(bitmask)))
    number = num
    #print('Passed num is' + str(hex(num)))
    var_value = number & bitmask
    #print('Var value is' + str(hex(var_value)))
    number = number >> bits_to_get_from_lsb
    #print('the input byte is now ' + str(hex(number)))
    return (number, var_value)

print('Enter the byte stream in hex')
byte_stream = input()
byte_string = byte_stream.replace(" ", "")
#print('byte_string is ' + byte_string)
bytes = [byte_string[i:i+2] for i in range(0, len(byte_string), 2)]
count = 0
linecount = 0
index = 0
already_incremented = 0
hit_x_mt_first_time = 0
one_byte = bytes[index]
#print('first byte from left ' + str(one_byte))
one_byte = int(one_byte, 16)
#print('first byte from left in hex' + str(hex(one_byte)))

	
path = 'C:\\Python_programs'
for infile in glob.glob( os.path.join(path, 'sample*') ):
    with open(infile) as f:
        for line in f:
            line1 = line.replace(" ", "")
            x = re.findall(r':(\w+)', str(line1))
            if x == []:
                #print('Nothing in list, its a byte')
                #print('already_incremented = ' + str(already_incremented))
                if hit_x_mt_first_time == 0:
                    #print('Hittin it the first time')
                    hit_x_mt_first_time = 1
                    index = index + 1
                else:
                    if already_incremented == 0:
                        index = index + 1
                print('Index =' + str(index))
                var_value = int(one_byte)
                one_byte = bytes[index]
                one_byte = int(one_byte, 16)
                
            else:
                new_num, var_value = bit_ops(one_byte, int(x[0]))
                one_byte = new_num
                count = count + int(x[0])
            #print('bits covered so far ' + str(hex(count)))
            y = line1.split(':')
            print(y[0] + ' = ' + str(var_value))
            if count == 8:
                index = index + 1
                already_incremented = 1
                #print('Exiting Line for loop, 8 bits covered, Jumping to next byte')
                #print('Index now is =' + str(index))
                #print('Length of bytestring is =' + str(len(byte_string)))
                count = 0
                if index == (len(byte_string)/2):
                    #print('Done looping through all bytes.')
                    break
                if index < (len(byte_string)/2):
                    one_byte = bytes[index]
                    #print('Next byte from left ' + str(one_byte))
                    one_byte = int(one_byte, 16)
                    #print('Next byte from left in hex' + str(hex(one_byte)))             
                    
                    
                
                    
                   
                    
                    
                    
		    
		    
		        
                
