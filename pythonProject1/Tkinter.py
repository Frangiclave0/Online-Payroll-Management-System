from tkinter import ttk
from tkinter import *
import os
import errno
import sqlite3


class Products:
    db_name = r'.\db\database_products.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title('Products Application')

        # Creating a frame container
        frame = LabelFrame(self.wind, text='Register a new Product')
        frame.grid(row=0, column=0, columnspan=10, pady=30, padx=30)

        # Name Input
        Label(frame, text='Name: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)

        # Price Input
        Label(frame, text='Price: ').grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1, pady=2, padx=5)

        # Button add product
        ttk.Button(frame, text='Save Product', command=self.add_product).grid(row=3, columnspan=3, sticky=W + E, pady=2,
                                                                              padx=5)

        # Output messages
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=3, sticky=W + E)

        # Treeview / table
        height = 10
        self.tree = ttk.Treeview(height=height, columns=2, selectmode=BROWSE)
        self.tree.bind("<<TreeviewSelect>>", self.item_selected)
        self.tree.grid(row=4, column=0, columnspan=3, pady=2, padx=5)
        # headings table
        self.tree.heading('#0', text='Name', anchor=CENTER)
        self.tree.heading('#1', text='Price', anchor=CENTER)

        # Buttons
        ttk.Button(text='DELETE', command=self.delete_product).grid(row=5, column=0, sticky=W)
        ttk.Button(text='EDIT', command=self.edit_product).grid(row=5, column=1, columnspan=2, sticky=W+E)

        # load data
        self.get_products()

    def run_query(self, query, parameters=()):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, parameters)
                conn.commit()
            return result
        except sqlite3.Error as error:
            print(error)
            self.create_db()

    def get_products(self):
        # clean table
        self.clean_table()

        # quering data
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        # filling data
        try:
            for row in db_rows:
                self.tree.insert('', 0, text=row[1], values=row[2])
        except TypeError as te:
            self.message['text'] = self.message['text'] + "\nNo hay ningún producto"

    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0

    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?)'
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.get_products()
            self.message['text'] = 'Product {} added Successfully'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['text'] = 'Name and price is required'
            self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
            # Me aseguro que he seleccionado un registro
            self.tree.item(self.tree.selection())['text'][0]

            self.message['text'] = ''
            name = self.tree.item(self.tree.selection())['text']
            query = 'DELETE FROM product WHERE name = ?'
            self.run_query(query, (name,))
            self.message['text'] = 'Record "{}" deleted successfully'.format(name)
            self.get_products()
        except IndexError as e:
            print("error:", e)
            self.message['text'] = 'Please select a record'
            return

    def edit_product(self):
        self.message['text'] = ''
        try:
            # Me aseguro que he seleccionado un registro
            self.tree.item(self.tree.selection())['text'][0]

            name = self.tree.item(self.tree.selection())['text']
            old_price = self.tree.item(self.tree.selection())['values'][0]
            print(f"name: {name} / price: {old_price}")
            self.edit_wind = Toplevel()
            self.edit_wind.title = "Edit Product"

            # Old Name
            Label(self.edit_wind, text="Old Name:").grid(row=0, column=0, padx=10, pady=5)
            Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=name), state='readonly') \
                .grid(row=0, column=1)
            # New Name
            Label(self.edit_wind, text='New Name').grid(row=1, column=0, padx=10, pady=5)
            new_name = Entry(self.edit_wind)
            new_name.grid(row=1, column=1, padx=10, pady=5)
            # Old Price
            Label(self.edit_wind, text="Old Price:").grid(row=2, column=0, padx=10, pady=5)
            Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=old_price), state='readonly') \
                .grid(row=2, column=1)
            # New Price
            Label(self.edit_wind, text='New Price').grid(row=3, column=0, padx=10, pady=5)
            new_price = Entry(self.edit_wind)
            new_price.grid(row=3, column=1, padx=10, pady=5)
            # Button
            Button(self.edit_wind, text='Update',
                   command=lambda: self.edit_records(new_name.get(), new_price.get(), name)) \
                .grid(row=4, column=0, columnspan=2, sticky=W+E)

        except IndexError as e:
            self.message['text'] = 'Please select a record'
            return

    def edit_records(self, new_name, new_price, old_name):
        print(new_name, new_price, old_name)
        query = 'UPDATE product SET name = ?, price = ? WHERE name = ?'
        parameters = (new_name, new_price, old_name)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Record {} updated successfully'.format(new_name)
        self.get_products()

    # clean table
    def clean_table(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

    def create_db(self):
        try:
            os.mkdir('db')
        except OSError as e:
            print('Directorio ya existe')
            if e.errno != errno.EEXIST:
                raise

        conn = sqlite3.connect(self.db_name)  # You can create a new database by changing the name within the quotes
        c = conn.cursor()  # The database will be saved in the location where your 'py' file is saved
        c.execute('''
        CREATE TABLE "product" (
            "id"	INTEGER NOT NULL UNIQUE,
            "name"	TEXT NOT NULL,
            "price"	REAL NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT)
        )
        ''')
        self.message['text'] = 'Tabla creada con éxito'
        conn.commit()

    def item_selected(self, event):
        print(self.tree.item(self.tree.selection())['text'], self.tree.item(self.tree.selection())['values'])
        message = self.tree.item(self.tree.selection())
        self.message['text'] = 'Seleccionado {}'.format(message)


if __name__ == '__main__':
    window = Tk()
    application = Products(window)
    window.mainloop()