import sqlite3
con = sqlite3.connect('hrsystem.db')
cur = con.cursor()
cur.execute('CREATE TABLE Customer (cid real, cname text, age real)')
print("Table created successfully")
con.commit()
con.close()
input()