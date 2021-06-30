import urllib.request, urllib.error, urllib.parse
import re

def getContent(url):
    response = urllib.request.urlopen(url)
    webContent = response.read()
    return(str(webContent))

def trimText(text):
    trimmedText = text[text.find('"reddit: the front page of the internet"}'):]
    trimmedText = trimmedText[:trimmedText.find('"Popular Communities"')]

    trimmedText = re.sub(r'","upvoteRatio.*?https://www.reddit.com/r/', r'\n', trimmedText)
    trimmedText = re.sub(r'","upvoteRatio.*?$', r'\n', trimmedText)

    trimmedText = re.sub(r'"reddit: the front page of the internet"}.*?https://www.reddit.com/r/', r'\n', trimmedText)

    trimmedText = re.sub(r'/comments/.*?"title":', r'||||', trimmedText)

    trimmedText = re.sub(r'"title":', r'"title":\n\n', trimmedText)
    trimmedText = re.sub(r',"topAwardedType":"ACTIVE', r'', trimmedText)
    trimmedText = re.sub(r',"topAwardedType":"INACTIVE', r'', trimmedText)

    trimmedText = re.sub(r'\\x..', r'', trimmedText)
    trimmedText = re.sub(r'\\', r'', trimmedText)

    trimmedText = re.sub(r'"\n', r'\n', trimmedText)
    trimmedText = re.sub(r'\n"', r'\n', trimmedText)

    trimmedText = re.sub(r'"\|\|\|\|', r'||||', trimmedText)
    trimmedText = re.sub(r'\|\|\|\|"', r'||||', trimmedText)

    if '||||' not in trimmedText[0:49]:
        trimmedText = trimmedText[:trimmedText.find('\n')]

    return trimmedText

def sepHeadlines(text):
    text = text.split('\n')

    newText = []

    for element in text:
        if element != '' and element not in newText:
            newText.append(element)

    return newText