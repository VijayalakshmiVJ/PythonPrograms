
import os, zipfile

print('Enter the path where Zip files exist. Please note the extracted files will be placed in the same path under name unzipped files')
dir_name = input()
extension = ".zip"

os.chdir(dir_name) # change directory from working dir to dir with files
if not os.path.exists(dir_name +'\\unzipped_files'):
    os.makedirs(dir_name +'\\unzipped_files')
         
for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        target_dir = dir_name +'\\unzipped_files'
        zip_ref.extractall(target_dir) # extract file to dir
        zip_ref.close() # close file
        #os.remove(file_name) # delete zipped file
