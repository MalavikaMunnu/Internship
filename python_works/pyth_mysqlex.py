import mysql.connector

# conn=mysql.connector.connect(host="localhost",user="root",password="root")
# print(conn)
# cursor=conn.cursor()
# cur.execute("CREATE DATABASE mydb")



conn=mysql.connector.connect(host="localhost",user="root",password="root",db="mydb")
print(conn)
cur=conn.cursor()


# ------ TABLE CREATION ------

# cur.execute("CREATE TABLE contacts(id int primary key auto_increment,cname varchar(50),phone bigint)")
# print("table created")



# ------ INSERTION ------

# cur.execute("INSERT INTO contacts VALUES(null,'malavika',9876543210),(null,'nazri',9876543211),(null,'arjun',9876543212),(null,'shahil',9876543213)")
# conn.commit()
# print("values inserted")



# ------ SELECTION ------

cur.execute