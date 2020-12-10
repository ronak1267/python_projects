import mysql.connector

mydb = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='mycustomers')

cursor = mydb.cursor()

sql = "select * from customers"
cursor.execute(sql)

data = cursor.fetchall()

records = cursor.rowcount
print("\r\n You have " + str(records) + " records in your customer table. \r\n")



for i in data:
    print("\r\n customer id: " + str(i[0]) + "\r\n")
    print("\r\n customer name: " + i[1] + "\r\n")
    print("\r\n customer age: " + i[2] + "\r\n")
    print("\r\n customer gender: " + i[3] + "\r\n")
