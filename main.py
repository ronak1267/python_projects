import mysql.connector
myfile = open("data.txt", "w+")

mydb = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='mycustomers')

cursor = mydb.cursor()

while(True):

    uname = input("Enter name : ")
    if uname == 'q':
        exit()


    uage = input("Enter age : ")
    ugender = input("Enter your gender : ")

    sql = "insert into customers(name, age, gender) values (%s, %s, %s)"
    vals = (uname, uage, ugender)
    cursor.execute(sql, vals)
    mydb.commit()


    myfile.write('\r\n Customer name : ' + uname + '\r\n')
    myfile.write('\r\n Customer age : ' + uage + '\r\n')
    myfile.write('\r\n customer gender : ' + ugender + '\r\n')
    print('data saved to file please type q to exit the program.')