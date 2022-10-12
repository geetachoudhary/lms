from db import DbConnection

class Users:
    
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile
    
    def create(self):
        statement = "INSERT INTO user (name, mobile) VALUES (%s, %s)"
        data = (self.name, self.mobile)
        cursor = DbConnection.getCursor()
        print(statement, data) 
        cursor.execute(statement, data)
        DbConnection.commit()

    @classmethod
    def getall(cls):
        statement = "SELECT * FROM user;"
        cursor = DbConnection.getCursor()
        cursor.execute(statement)
        result = cursor.fetchall()
        return result

    @classmethod
    def update_name(cls, name, id):
        statement = "UPDATE user set name = %s WHERE id = %s;"
        data = (name, id,)
        cursor = DbConnection.getCursor()
        cursor.execute(statement, data)
        DbConnection.commit()

    @classmethod
    def delete(self, id):
        statement = "DELETE FROM user WHERE id = %s;"
        data = (id,)
        cursor = DbConnection.getCursor()
        cursor.execute(statement, data)
        DbConnection.commit()
    
    def get_user_rent_fee(self, user_id):
        fee = 0
        statement = "SELECT DATEDIFF(rented_date, now()) FROM books where userId = %s and DATEDIFF(rented_date, now()) > 20;"
        data = (user_id,)
        cursor = DbConnection.getCursor()
        cursor.execute(statement, data)
        records = cursor.fetchall()
        for record in records:
            days = record[0]
            fee += 5*((days*(days+1)//2)-6)
        return fee
        
    
    @classmethod
    def get_input(cls):
        name = input("Enter username: ")
        mobile = input("Enter mobile number: ")
        return cls(name, mobile)

