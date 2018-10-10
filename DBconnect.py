import mysql.connector
class DBconnect:
    con=''
    def main():
        try:
            DBconnect.con=mysql.connector.connect(user='root',password='root',host='localhost',database='admin')
            print("connected....")
            cur=DBconnect.con.cursor()
            #cur.execute("create table data(name varchar(20), contactno int(10), dept varchar(15), salary int(20))")
            print("table created...")
            cur.execute("insert into data values('Ramesh',9665544,'Account',10000)")
            print("Record Inserted....")
            DBconnect.con.commit()
            print("comminted...")
            cur.execute('select * from data')
            DBconnect.con.rollback()
            print("rollback succes..")
        except Exception as e:
            print("Exception:",e)
        finally:
            if DBconnect.con !='':
                DBconnect.con.close()
                print("closed...")
if __name__=='__main__':
    DBconnect.main()
