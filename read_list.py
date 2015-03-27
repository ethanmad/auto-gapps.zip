import string

global app_list
global url_list
url_list = []

def read_list():
  f = open("app_list", "r")
  global app_list
  app_list = f.readlines()
  f.close()

def extract_info(line):
  # name = string.split(line, ":", 1)[0].strip()
  url = string.split(line, ":", 1)[1].strip()
  return url


# main method
def build_app_dictionary():
  read_list()
  for line in app_list:
    if line.isspace():
      continue
    global url_list
    url_list.append(extract_url(line))
  return url_list
