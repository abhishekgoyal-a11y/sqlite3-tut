import sqlite3

# create database
conn = sqlite3.connect("Database.db")

# cursor is used for performing action inside database like create tables,update,delete etc.
c = conn.cursor()


# c.execute(
#     "SELECT * FROM customers WHERE rowid=2 OR email='xyz@gmail.com'")

# c.execute(
#     "SELECT * FROM customers WHERE rowid=2 AND email='pqr@gmail.com'")

# c.execute(
#     "SELECT * FROM customers WHERE last_name LIKE 'pq%' ")

c.execute(
    "SELECT * FROM customers WHERE age<=20 ")

# three ways for fetching data
# 1. fetchone()
# 2. fetchmany(specify number of table)
# 3. fetchall()

print(c.fetchmany(3))

conn.commit()

# closing the commection
conn.close()
