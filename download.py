import urllib
# TODO: read in a text file containing file urls and file names, then download all files listed

def download(apk_url, number):
  urllib.urlretrieve(apk_url, str(number) + ".apk")
