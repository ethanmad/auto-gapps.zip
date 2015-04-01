import os
import zipfile
import time

zip_name = "gapps-" + time.strftime("%Y-%m-%d") + ".zip"
zip_dir = "./" + zip_name + "/"

def zipdir(path):
  if not os.path.exists(zip_dir):
    os.makedirs(zip_dir)
  zipf = zipfile.ZipFile(zip_name)
  for root, dirs, files in os.walk(path):
    for file in files:
      zipf.write(os.path.join(root, file))
  zipf.close()
