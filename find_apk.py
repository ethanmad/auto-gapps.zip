import httplib2
import string
from bs4 import BeautifulSoup

def load_page(url):
    http = httplib2.Http()
    headers = {'User-agent': 'Mozilla/5.0'} # bypass APK Mirror's user-agent check
    status, response = http.request(url, "GET", headers=headers)
    return response

def get_postarea(response):
    soup = BeautifulSoup(response)
    postarea = soup.findAll("div", { "class" : "post-area" })[0]
    return postarea

def get_url(string_to_split):
    return string.split(str(string_to_split), '"')[3]

def get_apk(app_url):
    # find url of newest upload page
    response = load_page(app_url)
    download = get_postarea(response).findAll("a", { "class" : "downloadLink"})[0]
    download_url =  "http://www.apkmirror.com" + get_url(download)

    # find actual download link for newest upload
    response2 = load_page(download_url)
    download2 = get_postarea(response2).findAll("a", { "type": "button" })[0]
    file_url = get_url(download2)
    return file_url
