import os
# import zipfile
# import requests

directory = "random_files"
url = "https://upload.itcollege.ee/~aleksei/random_files_without_extension.zip"

for i in os.listdir(directory):
    d = os.path.join(directory, i)
    with open(d, "rb") as f:
        file = f.read(3)
    if file == (b'\xff\xd8\xff'):
        print("jpeg found")
        os.rename(d, d + ".jpg") 
    else:
        os.remove(d)
