import sqlite3
con = sqlite3.connect('hrsystem.db')
cur = con.cursor()
cid = int(input("enter ID Customer: "))
isFound = False

for record in cur.execute('SELECT * FROM Customer WHERE cid='+str(cid)):
    print("CID=",record[0],"Cname= ",record[1],"CAge= ",record[2])
    break
if(isFound == False):
    print("Record does not exists")

con.close()
input()