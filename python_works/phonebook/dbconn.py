import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root",db='assignment')
print(conn)
cur=conn.cursor()
# cur.execute("CREATE DATABASE assignment")

# cur.execute("CREATE TABLE phonebook(id int primary key auto_increment,cname varchar(50),phone bigint)")

def addcontact(name,phone):
    query=f"INSERT INTO phonebook VALUES(null,'{name}',{phone})"
    print(query)
    cur.execute(query)
    conn.commit()
    return 1

def viewcontacts():
    query="SELECT * FROM phonebook"
    cur.execute(query)
    res=cur.fetchall()
    return res


# # # conn.close()