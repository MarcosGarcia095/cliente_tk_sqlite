import tkinter as tk
from app import Application
from customer_manager import CustomerManager
from database import Database

if __name__ == "__main__":
    db = Database("customers.db")           
    db.connect()                            
    db.create_table()                       

    manager = CustomerManager(db)           

    root = tk.Tk()                          
    app = Application(root, manager)        
    root.mainloop()                         
    db.close()                              