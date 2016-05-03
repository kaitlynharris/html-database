import sqlite3
import datetime

conn = sqlite3.connect('pagecontent.db')

def createTable():
    conn.execute('CREATE TABLE if not exists body_content( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        Body TEXT, \
        LastUse TEXT \
        );')

def newEntry(newbodytext):
    # store new body entry and datetime of page creation
    textdate = str(datetime.datetime.now())[0:10]
    sql_str = "INSERT INTO body_content (Body, LastUse) VALUES ('{}', '{}');".format(newbodytext, textdate)
    conn.execute(sql_str)
    conn.commit()

def viewAll():
    sql_str = "SELECT * from body_content"
    cursor = conn.execute(sql_str)

    # Get data from cursor in array
    rows = cursor.fetchall()
    return rows

def updateUse(choice):
    # update last use column if page is created using premade content
    textdate = str(datetime.datetime.now())
    sql_str = "UPDATE body_content SET LastUse = '{0}' where body_content = '{1}'".format(textdate, choice)

def deleteCharacter(change_id):
    sql_str = "DELETE from body_content where ID={}".format(change_id)
    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes

def main():
    createTable()
    newEntry('testing testing testing')

if __name__ == '__main__':
    main()
