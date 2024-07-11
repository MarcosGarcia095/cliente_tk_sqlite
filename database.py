import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)        
        self.connection.execute("PRAGMA foreign_keys = 1")     

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """
        self.execute(query)                                     

    def execute(self, query, params=()):
        with self.connection:                                   
            cursor = self.connection.cursor()                   
            cursor.execute(query, params)                       
            self.connection.commit()                            

    def fetch_one(self, query, params=()):                      
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()                                

    def fetch_all(self, query, params=()):                    
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()                                

    def close(self):                                            
        if self.connection:
            self.connection.close()