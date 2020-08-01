import sqlite3

# create database
conn = sqlite3.connect("Database.db")

# cursor is used for performing action inside database like create tables,update,delete etc.
c = conn.cursor()

# update record

c.execute(
    """UPDATE customers SET first_name='xyz' WHERE rowid=2 """
)

conn.commit()

# closing the commection
conn.close()
