import tkinter
from tkinter import ttk
from tkinter import *
import sqlite3


class Payroll:
    # db_name = 'Payroll.db'

    def __init__(self, window, title):
        """
        """
        self.window = window
        self.window.title(title)
        self.window.geometry("1018x345+200+100")
        self.lblTitle = tkinter.Label(self.window,
                                      text="Online Employee Payroll Management System", font=("Arial Narrow", 20))
        self.lblTitle.place(x=270, y=20)
        self.lblRecord = tkinter.Label(self.window, text="Records:")
        self.lblRecord.grid(pady=50)
        self.db = sqlite3.connect('Payrolls.db')
        # Set Class Tree
        self.tree = self._construct_tree()

    def __del__(self):
        """
        """
        pass

    def _construct_tree(self):
        """
        """
        tree = ttk.Treeview(self.window)
        # Format Column
        tree['columns'] = ("Emp_ID",
                           "Dept_ID",
                           "Last_Name",
                           "First_Name",
                           "Middle_Name",
                           "Emp_Address",
                           "Emp_Email",
                           "Bonus",
                           "Taxes"
                           )
        tree.column("#0", width=0, stretch=NO)
        tree.column("Emp_ID", anchor=CENTER, width=100)
        tree.column("Dept_ID", anchor=CENTER, width=100)
        tree.column("Last_Name", anchor=CENTER, width=100)
        tree.column("First_Name", anchor=CENTER, width=120)
        tree.column("Middle_Name", anchor=CENTER, width=120)
        tree.column("Emp_Address", anchor=W, width=140)
        tree.column("Emp_Email", anchor=W, width=120)
        tree.column("Bonus", anchor=W, width=100)
        tree.column("Taxes", anchor=W, width=100)

        # Create Heading
        tree.heading("#0", text="", anchor=W)
        tree.heading("Emp_ID", text="Emp_ID", anchor=CENTER)
        tree.heading("Dept_ID", text="Dept_ID", anchor=CENTER)
        tree.heading("Last_Name", text="Last_Name", anchor=CENTER)
        tree.heading("First_Name", text="First_Name", anchor=CENTER)
        tree.heading("Middle_Name", text="Middle_Name", anchor=CENTER)
        tree.heading("Emp_Address", text="Emp_Address", anchor=W)
        tree.heading("Emp_Email", text="Emp_Email", anchor=W)
        tree.heading("Bonus", text="Bonus", anchor=W)
        tree.heading("Taxes", text="Taxes", anchor=W)

        tree.place(x=10, y=70)

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree)
        tree_scroll.place(x=300, y=300)

        addButton = Button(self.window, text="Add", command=self.add)
        addButton.place(x=400, y=300)

        editButton = Button(self.window, text="Edit")
        editButton.place(x=450, y=300)

        deleteButton = Button(self.window, text="Delete")
        deleteButton.place(x=500, y=300)

        return tree

    def add(self):
        def submit():
            # Connection
            # connection = sqlite3.connect('Payroll.db')
            connection = self.db

            # Create Cursor
            cursor = connection.cursor()

            # Insert into the Table
            cursor.execute("INSERT INTO Employee VALUES (:Emp_ID, :Last_Name, :First_Name,"
                           " :Middle_Name, :Emp_Address, :Emp_Email, :Dept_ID,:Bonus, :Taxes)",
                           {
                               'Emp_ID': txtEmpID.get(),
                               'Last_Name': txtLName.get(),
                               'First_Name': txtFName.get(),
                               'Middle_Name': txtMName.get(),
                               'Emp_Address': txtAddress.get(),
                               'Emp_Email': txtEmail.get(),
                               'Dept_ID': txtDeptID.get(),
                               'Bonus': txtBonus.get(),
                               'Taxes': txtTaxes.get()
                           })
            #might edit this out later
            #cursor.execute("INSERT INTO Payroll VALUES (:Bonus, :Taxes)",
            #               {
            #                  'Bonus': txtBonus.get(),
            #                   'Taxes': txtTaxes.get(),
            #                  'Salary_ID':
            #              })

            # Commit our Command
            connection.commit()

            # Close our Connection
            connection.close()

            # Clear text
            txtEmpID.delete(0, END)
            txtDeptID.delete(0, END)
            txtFName.delete(0, END)
            txtMName.delete(0, END)
            txtLName.delete(0, END)
            txtEmail.delete(0, END)
            txtAddress.delete(0, END)
            txtBonus.delete(0, END)
            txtTaxes.delete(0, END)

        # Adds new Window
        self.window_2 = Toplevel(self.window)
        self.window_2.geometry("700x300+300+100")
        self.window_2.title('Add in Database')

        lblEmpID = tkinter.Label(self.window_2, text="Emp_ID:")
        txtEmpID = tkinter.Entry(self.window_2)
        lblEmpID.grid(row=0, column=2, pady=20)
        txtEmpID.grid(row=0, column=3, pady=20)

        lblDeptID = tkinter.Label(self.window_2, text="Dept_ID:")
        txtDeptID = tkinter.Entry(self.window_2)
        lblDeptID.grid(row=0, column=4)
        txtDeptID.grid(row=0, column=5)

        lblFName = tkinter.Label(self.window_2, text="First Name:")
        txtFName = tkinter.Entry(self.window_2)
        lblFName.grid(row=1, column=1, pady=20)
        txtFName.grid(row=1, column=2, pady=20)

        lblMName = tkinter.Label(self.window_2, text="Middle Name:")
        txtMName = tkinter.Entry(self.window_2)
        lblMName.grid(row=1, column=3)
        txtMName.grid(row=1, column=4)

        lblLName = tkinter.Label(self.window_2, text="Last Name:")
        txtLName = tkinter.Entry(self.window_2)
        lblLName.grid(row=1, column=5)
        txtLName.grid(row=1, column=6)

        lblEmail = tkinter.Label(self.window_2, text="Email:")
        txtEmail = tkinter.Entry(self.window_2)
        lblEmail.grid(row=2, column=1, pady=20)
        txtEmail.grid(row=2, column=2, pady=20)

        lblAddress = tkinter.Label(self.window_2, text="Home Address:")
        txtAddress = tkinter.Entry(self.window_2)
        lblAddress.grid(row=2, column=3)
        txtAddress.grid(row=2, column=4)

        lblBonus = tkinter.Label(self.window_2, text="Bonus:")
        txtBonus = tkinter.Entry(self.window_2)
        lblBonus.grid(row=2, column=5)
        txtBonus.grid(row=2, column=6)

        lblTaxes = tkinter.Label(self.window_2, text="Taxes:")
        txtTaxes = tkinter.Entry(self.window_2)
        lblTaxes.grid(row=3, column=3)
        txtTaxes.grid(row=3, column=4)

        btnSubmit = tkinter.Button(self.window_2, text="Submit", command=submit)
        btnSubmit.place(x=300, y=220)


if __name__ == '__main__':
    # Create the main/parent window name root
    # root = tkinter.Tk()
    window = Tk()
    application = Payroll(window,
                           "Online Employee Payroll Management System"
                           )
    window.mainloop()

