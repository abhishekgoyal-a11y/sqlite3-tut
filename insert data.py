import sqlite3

# create database
conn = sqlite3.connect("Database.db")

# cursor is used for performing action inside database like create tables,update,delete etc.
c = conn.cursor()

# insert single data at a time into table
# c.execute(
#     "INSERT INTO customers VALUES('xyz', 'xyz', 'xyz@GMAIL.COM', 23)")

# insert many data at a time into table
many_datas = [
    ("das", "poi", "lfd.kjg@gmail.com", 10),
    ("dsa", "zys", "zyz.xyz@gmail.com", 13),
    ("pqr", "r", "pqr@gmail.com", 25)
]
c.executemany(
    "INSERT INTO customers VALUES(?,?,?,?)", many_datas)

print("succes")
conn.commit()

# closing the commection
conn.close()
