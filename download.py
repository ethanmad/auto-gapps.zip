import urllib
import os

save_directory = "./gapps/"
def download(apk_url, number):
  if not os.path.exists(save_directory):
    os.makedirs(save_directory)
  urllib.urlretrieve(apk_url, save_directory + str(number) + ".apk")
