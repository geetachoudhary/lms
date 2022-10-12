from db import DbConnection

class Books:
    
    def __init__(self, name, author, publication, id):
        self.id = None
        self.name = name
        self.author = author
        self.publication = publication


    def create(self):
        statement = "INSERT INTO books (name, author, publicatin) VALUES (%s, %s, %s)"
        data = (self.name, self.author, self.publication)
        cursor = DbConnection.getCursor()
        print(statement, data) 
        cursor.execute(statement, data)
        DbConnection.commit()

    @classmethod
    def getall(cls):
        statement = "SELECT * FROM books;"
        cursor = DbConnection.getCursor()
        cursor.execute(statement)
        result = cursor.fetchall()
        return result

    @classmethod
    def update_name(cls, name, id):
        statement = "UPDATE books set name = %s WHERE id = %s;"
        data = (name, id,)
        cursor = DbConnection.getCursor()
        cursor.execute(statement, data)
        DbConnection.commit()

    @classmethod
    def delete(self, id):
        statement = "DELETE FROM books WHERE id = %s;"
        data = (id,)
        cursor = DbConnection.getCursor()
        cursor.execute(statement, data)
        DbConnection.commit()
    
    def get_book_rent_fee(self, book_id):
        fee = 0
        statement = "SELECT DATEDIFF(rented_date, now()) FROM books where id = %s and DATEDIFF(rented_date, now()) > 20;"
        data = (book_id,)
        cursor = DbConnection.getCursor()
        cursor.execute(statement, data)
        records = cursor.fetchall()
        for record in records:
            days = record[0]
            fee += 5*((days*(days+1)//2)-6)
        return fee
    
    @classmethod
    def rent_to_user(self, userId, bookId):
        try:
            statement = "UPDATE books set user_id = %s, rented_date = now() WHERE id = %s and userId != %s;"
            data = (userId, bookId, userId)
            cursor = DbConnection.getCursor()
            cursor.execute(statement, data)
            DbConnection.commit()
        except:
            print("Book cannot be rented right now. Please try after couple of days.")
    
    def clear_rented_book(cls, bookId):
        statement = "UPDATE books set user_id = null, rented_date = null WHERE id = %s;"
        data = (bookId,)
        cursor = DbConnection.getCursor()
        cursor.execute(statement, data)
        DbConnection.commit()

    @classmethod
    def get_input(cls):
        name = input("Enter name: ")
        author = input("Enter author: ")
        publication = input("Enter publication: ")
        return cls(name, author, publication)

