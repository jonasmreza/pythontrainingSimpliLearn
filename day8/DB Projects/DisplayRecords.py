import sqlite3
con = sqlite3.connect('hrsystem.db')
cur = con.cursor()
for record in cur.execute('SELECT * FROM Customer'):
    print("CID=", record[0])
    print("Cname= ",record[1])
    print("CAge= ",record[2])

con.close()
input()
