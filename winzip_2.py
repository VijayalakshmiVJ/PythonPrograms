

import zipfile


with zipfile.ZipFile("ME0001.zip","r") as zip_ref:
    zip_ref.extractall("D:\\userdata\\vijs\\Desktop\\testing_zip\\unzipped_files")
