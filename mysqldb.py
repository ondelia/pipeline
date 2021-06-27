import mysql.connector as sq

def connectToDatabase(host, user, passwd, buffered):
    mydb = sq.connect(host=host, user=user, passwd=passwd, buffered=buffered)
    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")
    for db in mycursor:
        print(db)

    mycursor.execute("SELECT COUNT(*) FROM frontpage.Headlines")
    result = mycursor.fetchall()
    print(result)

    mycursor.execute("select * from frontpage.Headlines")
    result = mycursor.fetchall()
    for row in result:
        print(row)

    return mydb, mycursor