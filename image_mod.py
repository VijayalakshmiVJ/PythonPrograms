#PIL image modification


import os
from PIL import Image

dir_name = 'D:\\userdata\\vijs\\Desktop'
os.chdir(dir_name)

catIm = Image.open('zophie.png')

catsize = catIm.size

print(catsize)

format = catIm.format_description

print(format)

catIm.save('zophie.jpg')
