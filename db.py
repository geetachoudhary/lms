import mysql.connector

class DbConnection:
    connection = None

    def __init__(self):
        pass
    
    @classmethod
    def createDbConnection(self):
        if self.connection is not None:
            return self.connection
        
        self.connection = mysql.connector.connect(
            host='localhost',
            database='lms',
            user='root',
            password=''
        )
        
        if self.connection.is_connected():
            db_Info = self.connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
        
        return self.connection
    
    @classmethod
    def getCursor(self):
        return self.connection.cursor()

    @classmethod
    def commit(cls):
        cls.connection.commit()

