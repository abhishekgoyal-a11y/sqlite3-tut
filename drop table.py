import sqlite3

# create database
conn = sqlite3.connect("Database.db")

# cursor is used for performing action inside database like create tables,update,delete etc.
c = conn.cursor()

# delete table

c.execute(
    """DROP TABLE customers """
)

conn.commit()

# closing the commection
conn.close()
