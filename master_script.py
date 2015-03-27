import read_list, download
import find_apk
# This script runs the other scripts.
# Sequence is as follows:
#   1) Read app_list and store names and URLs in memory.
#   2) Pass URLs into find_apk.py to get the APK URLs (store in memory).
#   3) Pass in APKs to download.py.
#   4) Put the APKs into a folder and make flashable ZIP.

# Read app_list to get url_list
url_list =  read_list.build_app_dictionary()

# Get list of file urls
for url in url_list:
    find_apk.get_apk(url)

# Download files
