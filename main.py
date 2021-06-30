from downloadpage import *
from mysqldb import *
from loadinfo import *
from datetime import datetime
from shutil import copyfile

print("Hello world!")
host, user, password, source, destination = loadinfo()

#1. The Python script will download the front page of Reddit.
fulltext = getContent('http://www.reddit.com')

#2. The script will parse the JSON, HTML, or CSV file to separate the headline and the subreddit on which it appeared. It will clean the data, add a time stamp column, and add a source column that says "Reddit".
trimmedtext = trimText(fulltext)

with open('reddit.csv', 'w') as f:
    f.write('')

headlines = sepHeadlines(trimmedtext)
now = datetime.utcnow()
myTime = now.strftime("%Y-%m-%d-%H%M%S")
headlinesOnly = ''

for element in headlines:
    print(element)
    with open('reddit.csv', 'a') as f:
        f.write(element + '||||Reddit||||' + myTime + '\n')

    element = element[element.find('||||'):]
    element = element[4:]

    headlinesOnly = headlinesOnly + ' ' + element
    print(element)

headlinesOnly = headlinesOnly.lower()
headlinesOnly = "".join([ch for ch in headlinesOnly if ch in 'abcdefghijklmnopqrstuvwxyz '])
print(headlinesOnly)

#3. On AWS, there will be a database and table called Headline to load this data. There will also be a table called Wordcount to count the words in the headlines.
#4. The Python script will access the database using environmental variables, and insert a row into the Headline table for each headline.

mydb, mycursor = connectToDatabase(host, user, password)

destination = destination.replace('TEST.csv', myTime + '.csv')
copyfile(source, destination)

insertNewHeadlines(mydb, mycursor, destination)

#5. The Python script will increment the words in the Wordcount for each word in a headline.
updateWordcount(mydb, mycursor, headlinesOnly, myTime)


#6. The Python script will store the data file locally and on S3.
