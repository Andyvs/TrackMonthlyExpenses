import sqlite3

conn = sqlite3.connect('usrdet.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE users
             (USER_ID text primary key, FIRST_NAME text, LAST_NAME text, DOB text, GENDER text, PASSWORD text, role text)''')

c.execute('''CREATE TABLE purchase
	         (USER_ID text, product text, quantity integer, unitprice integer, date text, purchase_idn INTEGER PRIMARY KEY AUTOINCREMENT, FOREIGN KEY(USER_ID) REFERENCES users(USER_ID))''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
