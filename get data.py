import sqlite3

# create database
conn = sqlite3.connect("Database.db")

# cursor is used for performing action inside database like create tables,update,delete etc.
c = conn.cursor()

# get data from table
# c.execute("SELECT * FROM customers")

# get primary key
c.execute("SELECT rowid,* FROM customers")

# three ways for fetching data
# 1. fetchone()
# 2. fetchmany(specify number of table)
# 3. fetchall()

print(c.fetchmany(3))

conn.commit()

# closing the commection
conn.close()
