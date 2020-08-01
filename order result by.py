import sqlite3

# create database
conn = sqlite3.connect("Database.db")

# cursor is used for performing action inside database like create tables,update,delete etc.
c = conn.cursor()

# c.execute('''SELECT * FROM customers ORDER BY rowid DESC
# ''')

# c.execute('''SELECT rowid,* FROM customers ORDER BY age ASC
# ''')

c.execute('''SELECT rowid,* FROM customers ORDER BY last_name
''')

items = c.fetchall()
for item in items:
    print(item)

conn.commit()

# closing the commection
conn.close()
