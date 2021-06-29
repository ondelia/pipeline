import mysql.connector as sq

def connectToDatabase(host, user, passwd, buffered=True):
    mydb = sq.connect(host=host, user=user, passwd=passwd, buffered=buffered)
    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")
    for db in mycursor:
        print(db)

    mycursor.execute("USE frontpage")

    return mydb, mycursor

def insertNewHeadlines(mydb, mycursor, csvFile):
    # File MUST be stored locally with the database, or the script may not work properly.
    csvFile = csvFile.replace('\\', '/')
    mycursor.execute("SHOW VARIABLES LIKE 'secure_file_priv';")
    result = mycursor.fetchall()
    print(result)

    insertCommand = "LOAD DATA INFILE '" + csvFile + "' \
    INTO TABLE headlines \
    FIELDS TERMINATED BY '||||' \
    LINES TERMINATED BY '\\r\\n' \
    (category,headline,datasource,scraped);"

    print(insertCommand)
    mycursor.execute(insertCommand)

    mycursor.execute("SELECT * FROM frontpage.headlines")
    result = mycursor.fetchall()
    for row in result:
        print(row)

    print("COUNT AFTER INSERT:")
    mycursor.execute("SELECT COUNT(*) FROM frontpage.headlines")
    result = mycursor.fetchall()
    print(result)

    mydb.commit()