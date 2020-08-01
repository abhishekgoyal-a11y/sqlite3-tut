import sqlite3

# create database
conn = sqlite3.connect("Database.db")

# cursor is used for performing action inside database like create tables,update,delete etc.
c = conn.cursor()

# delete record

c.execute(
    """DELETE from customers WHERE email ='xyz@gmail.com' """
)

conn.commit()

# closing the commection
conn.close()
