#! trackit.py


import os, time
from pathlib import Path


print('Tracking compilation')
file_path = 'D:\PCU_code\IGWBTDSE.IMG'

#print('Enter the path where the images will be stored including the image name')

#file_path = input()

while not os.path.exists(file_path):
    time.sleep(5)

if os.path.isfile(file_path):
    print('Compilation done, sending mail')
else:
    raise ValueError("%s isn't a file!" % file_path)
