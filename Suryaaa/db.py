import mysql.connector as c
conn = c.connect(
    host='localhost',
    user='root',
    passwd='Surya@fedora1',
    database='Blog'
)
cursor=conn.cursor()
