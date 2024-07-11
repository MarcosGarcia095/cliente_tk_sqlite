import tkinter as tk
from tkinter import messagebox
from customer import Customer
from customer_manager import CustomerManager

class Application:                                         
    def __init__(self, root, manager: CustomerManager):     
        self.root = root                                    
        self.manager = manager                              
        self.root.title("Administrador de clientes")              
        self.create_menu()                                                      

    def create_menu(self):
        self.clear_window()                                                             
        menu = tk.Menu(self.root)                                                      
        self.root.config(menu=menu)                                                     
        customer_menu = tk.Menu(menu)                                                   
        menu.add_cascade(label="Cliente", menu=customer_menu)                          
        customer_menu.add_command(label="Agregar", command=self.add_customer)               
        customer_menu.add_command(label="borrar", command=self.delete_customer)
        customer_menu.add_command(label="Actualizar", command=self.update_customer)
        customer_menu.add_command(label="Buscar", command=self.search_customer)
        customer_menu.add_command(label="Listar todos los clientes", command=self.list_all_customers)

    def add_customer(self):                                                           
        self.clear_window()                                                          
        frame = tk.Frame(self.root)                                                   
        frame.pack()                                                                  

        tk.Label(frame, text="Nombre:").grid(row=0, column=0)                           
        name = tk.Entry(frame)                                                        
        name.grid(row=0, column=1)                                                   

        tk.Label(frame, text="Apellido:").grid(row=1, column=0)                         
        surname = tk.Entry(frame)
        surname.grid(row=1, column=1)

        tk.Label(frame, text="Direccion:").grid(row=2, column=0)
        address = tk.Entry(frame)
        address.grid(row=2, column=1)

        def save_customer():
            customer_id = self.manager.get_next_customer_id()                                       
            customer = Customer(customer_id, name.get(), surname.get(), address.get())             
            self.manager.insert_customer(customer)                                                  
            messagebox.showinfo("Un exito!", f"Cliente agregado exitosamente con su ID {customer_id}")    
            print(f"Added Customer: ID={customer_id}, Name={customer.name}, Surname={customer.surname}, Address={customer.address}")
            self.create_menu()                                                                      

        tk.Button(frame, text="Agregar cliente", command=save_customer).grid(row=3, columnspan=2)      

    def delete_customer(self):
        self.clear_window()
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Label(frame, text="Cliente ID:").grid(row=0, column=0)
        customer_id = tk.Entry(frame)                               
        customer_id.grid(row=0, column=1)                           

        def remove_customer():                                              
            self.manager.delete_customer(int(customer_id.get()))            
            messagebox.showinfo("Correcto!", "Cliente borrado satisfactoriamente") 
            print(f"Cliente borrado con su ID {customer_id.get()}")
            self.create_menu()

        tk.Button(frame, text="Borrar cliente", command=remove_customer).grid(row=1, columnspan=2) 

    def update_customer(self):
        self.clear_window()
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Label(frame, text="Cliente ID:").grid(row=0, column=0)
        customer_id = tk.Entry(frame)
        customer_id.grid(row=0, column=1)

        def load_customer():
            customer = self.manager.get_customer(int(customer_id.get()))  
            if customer:
                name.delete(0, tk.END)                                    
                name.insert(0, customer.name)                             
                surname.delete(0, tk.END)
                surname.insert(0, customer.surname)
                address.delete(0, tk.END)
                address.insert(0, customer.address)
            else:
                messagebox.showerror("Error", "Cliente no encontrado")

        tk.Button(frame, text="Cargar cliente", command=load_customer).grid(row=1, columnspan=2) 

        tk.Label(frame, text="Nombre:").grid(row=2, column=0)
        name = tk.Entry(frame)
        name.grid(row=2, column=1)

        tk.Label(frame, text="Apellido:").grid(row=3, column=0)
        surname = tk.Entry(frame)
        surname.grid(row=3, column=1)

        tk.Label(frame, text="Direccion:").grid(row=4, column=0)
        address = tk.Entry(frame)
        address.grid(row=4, column=1)

        def save_updated_customer():
            customer = Customer(int(customer_id.get()), name.get(), surname.get(), address.get())          #Crea una instancia con los datos actualizados
            self.manager.update_customer(customer)                                                         #Actualiza el cliente en el manager de clientes
            messagebox.showinfo("Un exito!", "Cliente actualizado satisfactoriamente")
            print(f"Updated Customer: ID={customer.customer_id}, Name={customer.name}, Surname={customer.surname}, Address={customer.address}")
            self.create_menu()

        tk.Button(frame, text="Actualizar cliente", command=save_updated_customer).grid(row=5, columnspan=2)   #Crea un boton para actualizar el cliente, que al presionarlo llama a la funcion "save_update_customer"

    def search_customer(self):
        self.clear_window()
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Label(frame, text="Cliente ID:").grid(row=0, column=0)
        customer_id = tk.Entry(frame)
        customer_id.grid(row=0, column=1)

        def find_customer():
            customer = self.manager.get_customer(int(customer_id.get()))       #Obtiene el cliente con el ID otorgado
            if customer:
                messagebox.showinfo("Cliente encontrado", f"Nombre: {customer.name}, Apellido: {customer.surname}, Direccion: {customer.address}")
                print(f"Found Customer: ID={customer.customer_id}, Name={customer.name}, Surname={customer.surname}, Address={customer.address}")
            else:
                messagebox.showerror("Error", "Cliente no encontrado")
                print(f"Customer with ID {customer_id.get()} not found")
            self.create_menu()

        tk.Button(frame, text="Buscar cliente", command=find_customer).grid(row=1, columnspan=2) #Crea un boton para buscar cliente que al presionar llama a la funcion "find_customer"
    def list_all_customers(self):
        self.clear_window()
        frame = tk.Frame(self.root)
        frame.pack()

        customers = self.manager.get_all_customers()        #Obtiene lista de todos los clientes
        for i, customer in enumerate(customers):            #Itera sobre la lista de clientes
            tk.Label(frame, text=f"ID: {customer.customer_id}, Nombre: {customer.name}, Apellido: {customer.surname}, Direccion: {customer.address}").grid(row=i, column=0)
            print(f"Customer: ID={customer.customer_id}, Name={customer.name}, Surname={customer.surname}, Address={customer.address}")

        tk.Button(frame, text="Volver", command=self.create_menu).grid(row=len(customers), column=0)  #Boton que al presionar nos devuelve al menú

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()