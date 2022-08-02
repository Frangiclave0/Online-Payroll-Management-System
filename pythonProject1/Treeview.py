import tkinter
from tkinter import ttk
from tkinter import *
import sqlite3

from Window1 import txtEmpID, txtFName, txtLName, txtMName, txtAddress, txtEmail, txtDeptID, txtBonus, txtTaxes


def submit():
    # Connection
    connection = sqlite3.connect('Payroll.db')

    # Create Cursor
    cursor = connection.cursor()
    # Insert into the Table
    cursor.execute("INSERT INTO Employee VALUES (:Emp_ID, :Last_Name, :First_Name,"
                   " :Middle_Name, :Emp_Address, :Emp_Email, :Dept_ID)",
                   {
                       'Emp_ID': txtEmpID.get(),
                       'Last_Name': txtLName.get(),
                       'First_Name': txtFName.get(),
                       'Middle_Name': txtMName.get(),
                       'Emp_Address': txtAddress.get(),
                       'Emp_Email': txtEmail.get(),
                       'Dept_ID': txtDeptID.get()
                   })

    cursor.execute("INSERT INTO Payroll VALUES (:Bonus, :Taxes)",
                   {
                       'Bonus': txtBonus.get(),
                       'Taxes': txtTaxes.get()
                   })

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


def Add():
    # Adds new Window
    root = Toplevel(root)
    root2.geometry("700x300+300+100")
    root2.title('Add in Database')

    lblEmpID = tkinter.Label(root2, text="Emp_ID:")
    txtEmpID = tkinter.Entry(root2)
    lblEmpID.grid(row=0, column=2, pady=20)
    txtEmpID.grid(row=0, column=3, pady=20)

    lblDeptID = tkinter.Label(root2, text="Dept_ID:")
    txtDeptID = tkinter.Entry(root2)
    lblDeptID.grid(row=0, column=4)
    txtDeptID.grid(row=0, column=5)

    lblFName = tkinter.Label(root2, text="First Name:")
    txtFName = tkinter.Entry(root2)
    lblFName.grid(row=1, column=1, pady=20)
    txtFName.grid(row=1, column=2, pady=20)

    lblMName = tkinter.Label(root2, text="Middle Name:")
    txtMName = tkinter.Entry(root2)
    lblMName.grid(row=1, column=3)
    txtMName.grid(row=1, column=4)

    lblLName = tkinter.Label(root2, text="Last Name:")
    txtLName = tkinter.Entry(root2)
    lblLName.grid(row=1, column=5)
    txtLName.grid(row=1, column=6)

    lblEmail = tkinter.Label(root2, text="Email:")
    txtEmail = tkinter.Entry(root2)
    lblEmail.grid(row=2, column=1, pady=20)
    txtEmail.grid(row=2, column=2, pady=20)

    lblAddress = tkinter.Label(root2, text="Home Address:")
    txtAddress = tkinter.Entry(root2)
    lblAddress.grid(row=2, column=3)
    txtAddress.grid(row=2, column=4)

    lblBonus = tkinter.Label(root2, text="Bonus:")
    txtBonus = tkinter.Entry(root2)
    lblBonus.grid(row=2, column=5)
    txtBonus.grid(row=2, column=6)

    lblTaxes = tkinter.Label(root2, text="Taxes:")
    txtTaxes = tkinter.Entry(root2)
    lblTaxes.grid(row=3, column=3)
    txtTaxes.grid(row=3, column=4)

    btnSave = tkinter.Button(root2, text="Submit", command=submit)
    btnSave.place(x=320, y=220)


# Create the main/parent window name root
root = tkinter.Tk()
# Window Placement and Resize... geometry(XxY+X+Y)
root.geometry("992x338+300+100")
# assigning title to the Window
root.title("Online Employee Payroll Management System")
lblTitle = tkinter.Label(root, text=
"Online Employee Payroll Management System",
                         font=("Arial Narrow", 20))
lblTitle.place(x=270, y=20)

lblRecord = tkinter.Label(root, text="Record:")
lblRecord.grid(pady=50)

tree = ttk.Treeview(root)

# Format Column
tree['columns'] = ("Emp_ID", "Dept_ID", "Last_Name", "First_Name", "Middle_Name",
                   "Emp_Address", "Emp_Email", "Bonus", "Taxes")
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

tree.place(x=0, y=70)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree)
tree_scroll.place(x=300, y=300)

addButton = Button(root, text="Add", command=Add)
addButton.place(x=400, y=300)

editButton = Button(root, text="Edit")
editButton.place(x=450, y=300)

deleteButton = Button(root, text="Delete")
deleteButton.place(x=500, y=300)

root.mainloop()
