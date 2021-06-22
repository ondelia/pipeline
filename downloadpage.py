import urllib.request, urllib.error, urllib.parse

def getContent(url):
    response = urllib.request.urlopen(url)
    webContent = response.read()
    return(webContent)