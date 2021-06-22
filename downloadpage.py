import urllib.request, urllib.error, urllib.parse
import re

def getContent(url):
    response = urllib.request.urlopen(url)
    webContent = response.read()
    return(str(webContent))

def trimText(text):
    trimmedText = text[text.find('"reddit: the front page of the internet"}'):]
    trimmedText = trimmedText[:trimmedText.find('"Popular Communities"')]

    trimmedText = re.sub(r'"title":', r'"title":\n', trimmedText)
    trimmedText = re.sub(r'","upvoteRatio.*?"title":', r'', trimmedText)
    trimmedText = re.sub(r'"reddit: the front page of the internet"}.*?"title":', r'', trimmedText)
    trimmedText = re.sub(r',"topAwardedType":"ACTIVE', r'', trimmedText)
    trimmedText = re.sub(r',"topAwardedType":"ACTIVE', r'', trimmedText)

    trimmedText = re.sub(r'"\n', r'\n', trimmedText)
    trimmedText = re.sub(r'\n"', r'\n', trimmedText)

    return trimmedText

def sepHeadlines(text):
    text = text.split('\n')

    newText = []

    for element in text:
        if element != '' and element not in newText:
            newText.append(element)

    return newText

