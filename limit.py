import sqlite3

# create database
conn = sqlite3.connect("Database.db")

# cursor is used for performing action inside database like create tables,update,delete etc.
c = conn.cursor()


# c.execute('''SELECT rowid,* FROM customers WHERE last_name='Goyal' LIMIT 2
# ''')

c.execute('''SELECT rowid,* FROM customers LIMIT 2
''')

items = c.fetchall()
for item in items:
    print(item)

conn.commit()

# closing the commection
conn.close()
