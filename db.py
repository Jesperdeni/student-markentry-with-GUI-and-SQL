import mysql.connector

class mysqldb:
    def myDB(self):
        dbcon=mysql.connector.connect(
            host="192.168.29.244",
            user="test01",
            password="test@123",
            database="deni"
        )
        return dbcon
    
    def insertrecord(self,v1,v2,v3,v4,v5,v6,v7,v8):
        print("value passed",v1,v2,v3,v4,v5,v6,v7,v8)
        dbcon=self.myDB()
        cursor=dbcon.cursor()

        statement="INSERT INTO mark_entry(Student_name,Department,shift,Mark1,Mark2,Mark3,Mark4,Mark5)VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
        cursor.execute(statement,(v1,v2,v3,v4,v5,v6,v7,v8))
        dbcon.commit()
        dbcon.close()

    def deleterecord(self,v1):
        dbcon=self.myDB()
        cursor=dbcon.cursor()
        statement="DELETE FROM mark_entry WHERE Student_name=%s;"
        cursor.execute(statement,(v1,))
        dbcon.commit()
        dbcon.close()



    def selectrecord(self):
        dbcon=self.myDB()
        cursor=dbcon.cursor()
        statement="SELECT * FROM mark_entry;"
        cursor.execute(statement)
        result=cursor.fetchall()
        dbcon.close()
        return result


    



        
    

  

    