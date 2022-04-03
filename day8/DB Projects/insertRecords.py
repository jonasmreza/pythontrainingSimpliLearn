import sqlite3

con = sqlite3.connect("hrsystem.db")
cur = con.cursor()
cur.execute("Insert into Customer values (102,'qreli',20)")
print("Details inserted")
con.commit()
con.close()
input()