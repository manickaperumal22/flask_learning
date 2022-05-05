import sqlite3
connection=sqlite3.Connection("addressbook.db")
print("database opened successfully")
cursor=connection.cursor()
cursor.execute('''DROP TABLE address;''')
cursor.execute("create table address(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT UNIQUE NOT NULL,address TEXT NOT NULL)")
print("table created successfully")
connection.close()