from customer import Customer
from database import Database

class CustomerManager:                          
    def __init__(self, database: Database):     
        self.database = database                

    def get_next_customer_id(self):
        query = "SELECT MAX(customer_id) FROM customers"           
        result = self.database.fetch_one(query)                    
        next_id = result[0] + 1 if result[0] else 100              
        return next_id

    def insert_customer(self, customer: Customer):
        query = "INSERT INTO customers (customer_id, name, surname, address) VALUES (?, ?, ?, ?)"   
        params = (customer.customer_id, customer.name, customer.surname, customer.address)          
        self.database.execute(query, params)                                                        

    def update_customer(self, customer: Customer):
        query = "UPDATE customers SET name = ?, surname = ?, address = ? WHERE customer_id = ?"     
        params = (customer.name, customer.surname, customer.address, customer.customer_id)  
        self.database.execute(query, params)

    def delete_customer(self, customer_id: int):
        query = "DELETE FROM customers WHERE customer_id = ?"       
        self.database.execute(query, (customer_id,))                

    def get_customer(self, customer_id: int):
        query = "SELECT * FROM customers WHERE customer_id = ?"     
        result = self.database.fetch_one(query, (customer_id,))     
        if result:
            return Customer(*result)
        return None

    def get_all_customers(self):
        query = "SELECT * FROM customers"
        results = self.database.fetch_all(query)                    
        return [Customer(*result) for result in results]            