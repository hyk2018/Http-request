## This is a file that excutes CRUD (create, read, update, delete) operations in a PostgreSQL database

import psycopg2
conn=psycopg2.connect(
    database="myfirst",
    user="hyk",
    password="123456",
    host="localhost",
    port="5432"
)

print("connected to postgres")

#format: conn = psycopg2.connect(dbname="postgres", user="",password="", host="127.0.0.1", port="5432")

cur = conn.cursor()

#C
cur.execute("insert into cities(name,location) values('CZ','(120,110)')")
#R
cur.execute("select * from cities")
#U
cur.execute("update cities set name='Changzhou' where name='CZ'")
#D
cur.execute("delete from cities where name='Changzhou'")



rows = cur.fetchall()


print('//////////////////////////')
for row in rows:
    print('name=' + str(row[0]) + ' location=' + str(row[1]))
print('//////////////////////////\n')

conn.commit()
conn.close()
