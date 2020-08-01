import sqlite3
# create database in memory , it will not save in database
# conn = sqlite3.connect(":memory:")

# create database
conn = sqlite3.connect("Database.db")

# cursor is used for performing action inside database like create tables,update,delete etc.
c = conn.cursor()

# create table
c.execute('''CREATE TABLE customers (
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    age REAL
)

''')
conn.commit()

# closing the commection
conn.close()

# DATATYPES
# NULL
# INTEGER (2,3,4,5)
# REAL (2.3,1.0,3.9)
# TEXT
# BLOB
