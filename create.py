import sqlite3


def executeQuery(cursor,query,*args):
    try:
        if len(args) > 0:
            cursor.execute(query,args[0])
        else:
            response = cursor.execute(query)
            for row in response:
                print(row)
    except:
        print("error")
    

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_users_table = "CREATE TABLE IF NOT EXISTS USERS (id INTEGER PRIMARY KEY, username text, password text)"
create_items_table = "CREATE TABLE IF NOT EXISTS ITEMS (id INTEGER PRIMARY KEY, name text, price real)"
executeQuery(cursor,create_users_table)
executeQuery(cursor,create_items_table)


connection.commit()
connection.close()


