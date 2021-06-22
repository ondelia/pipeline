# Data Pipeline Project
This project will extract data from a source, transform it, and load it into a database.

Requirements for v1.0.0
1. The Python script will download the front page of Reddit.
2. The script will parse the JSON, HTML, or CSV file to separate the headline and the subreddit on which it appeared. It will clean the data, add a time stamp column, and add a source column that says "Reddit".
3. On AWS, there will be a database and table called Headline to load this data. There will also be a table called Wordcount to count the words in the headlines.
4. The Python script will access the database using environmental variables, and insert a row into the Headline table for each headline.
5. The Python script will increment the words in the Wordcount for each word in a headline.
6. The Python script will store the data file locally and on S3.
7. Test cases to cover all common scenarios.
8. Version control.


Requirements for v1.1.0
1. After downloading and parsing the data, atomic-write the data to a separate file. Save both the raw file and the cleaned data.
2. Schedule this job to run once every 12 hours.
3. Write a script to verify that the Wordcount table is correct (check it against the data in S3), and schedule it to run once per week.
4. Modify the script to also pull the headlines from CNN every 12 hours, and add them to the Headline table too.