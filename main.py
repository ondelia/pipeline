from downloadpage import *
from mysqldb import *
from loadinfo import *

print("Hello world!")

#1. The Python script will download the front page of Reddit.
fulltext = getContent('http://www.reddit.com')

#2. The script will parse the JSON, HTML, or CSV file to separate the headline and the subreddit on which it appeared. It will clean the data, add a time stamp column, and add a source column that says "Reddit".
trimmedtext = trimText(fulltext)

with open('reddit.txt', 'w') as f:
    f.write('')

headlines = sepHeadlines(trimmedtext)
for element in headlines:
    print(element)
    with open('reddit.txt', 'a') as f:
        f.write(element + '\n')

#3. On AWS, there will be a database and table called Headline to load this data. There will also be a table called Wordcount to count the words in the headlines.
#4. The Python script will access the database using environmental variables, and insert a row into the Headline table for each headline.

host, user, password = loadinfo()
mydb, mycursor = connectToDatabase(host, user, password, buffered=True)



#5. The Python script will increment the words in the Wordcount for each word in a headline.
#6. The Python script will store the data file locally and on S3.
