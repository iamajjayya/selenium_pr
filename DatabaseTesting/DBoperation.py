# import mysql.connector
#
# con   = mysql.connector.connect(host='localhost', port=3306, user='root', passwd='root', database ='student')
# cursor = con.cursor()
# cursor.execute("insert into student_details values(101,'Hemavathi')")
# con.commit()
# con.close()

import mysql.connector

con   = mysql.connector.connect(host='localhost', port=3306, user='root', passwd='root', database ='student')
cursor =  con.cursor()
cursor.execute("select * from student_details")
for row in cursor:
    print(row[0],row[1])


con.close()