from db import DbConnection

class Librarian:
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile
    
    def create(self):
        statement = "INSERT INTO librarian (name, mobile) VALUES (%s, %s)"
        data = (self.name, self.mobile)
        cursor = DbConnection.getCursor()
        print(statement, data) 
        cursor.execute(statement, data)
        DbConnection.commit()

    @classmethod
    def getall(cls):
        statement = "SELECT * FROM librarian;"
        cursor = DbConnection.getCursor()
        cursor.execute(statement)
        result = cursor.fetchall()
        return result

    @classmethod
    def update_name(cls, name, id):
        statement = "UPDATE librarian set name = %s WHERE id = %s;"
        data = (name, id,)
        cursor = DbConnection.getCursor()
        cursor.execute(statement, data)
        DbConnection.commit()

    @classmethod
    def delete(self, id):
        statement = "DELETE FROM librarian WHERE id = %s;"
        data = (id,)
        cursor = DbConnection.getCursor()
        cursor.execute(statement, data)
        DbConnection.commit()

    @classmethod
    def get_input(cls):
        name = input("Enter username: ")
        mobile = input("Enter mobile number: ")
        return cls(name, mobile)