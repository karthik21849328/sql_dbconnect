import mysql.connector

class Dbconect:
    def __init__(self):
        self.connection=None

    def connect_to_db(self):
        dict1={
            'host': '127.0.0.1',
            'user':'root',
            'password': 'root.123',
            'database':'revision'

        }
        self.connection=mysql.connector.connect(**dict1)
        if self.connection.is_connected():
            print("connection successful with db")


    def create_table(self,query):
            if not query:
                cursor=self.connection.cursor()
                cursor.execute(query)
                self.connection.commit()
                print("table created successfully")

    def insert_into(self,statement,params):
         if not params:
            cursor=self.connection.cursor()
            cursor.execute(statement,params)
            self.connection.commit()
            cursor.close()
            print("insertion successful")

    def insert_records(self):
        statement="""
                insert into revision.product(sku, name, price, created, last_updated) values(%s,%s,%s,%s,%s) """
        values=("pdoo1","google tv",85000.03,"2022-05-02","2023-05-01")

        statement1="""
                    insert into revision.product(name,price,sku,last_updated,created) values(%s,%s,%s,%s,%s)
                    """
        values1=("MITV",5000,"MI001","2020-05-25","2023-12-16")

        self.insert_into(statement,values)
        self.insert_into(statement1,values1)

    def delete_record(self,query):
            cursor=self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            cursor.close()
    
    def delete_record_from_table(self): 
        delete1="""
                delete from revision.product where sku=%s"""
        cursor=self.connection.cursor()
        cursor.execute(delete1,("pdoo1",))
        self.connection.commit()
        cursor.close()
         
         
        

        

    
      


if __name__=="__main__":
    dbconnection=Dbconect()  #creating object 
    dbconnection.connect_to_db()
    create_table1="""
    create table users(
        user_id int primary key,
        user_name varchar(30),
        user_phone varchar(30)
    )"""

    create_table2="""
            create table product(
            sku varchar(20),
            name varchar(20),
            price float,
            created date,
            last_updated date
            )"""
    dbconnection.create_table(create_table1)
    dbconnection.create_table(create_table2)
    dbconnection.insert_records()
    dbconnection.delete_record_from_table()

 