#import the tkinter module
import tkinter

# Create the parent window
window= tkinter.Tk()

#create the title for the window
window.title("Creating 3 Widgets - label, entry and button")

#creating a label widget (lblName)
lblName=tkinter.Label(window, text="Input Name:")

#creating a text entry widget (txtName)
txtName=tkinter.Entry(window)

#creating a button widget (called btnClick)
btnClick=tkinter.Button(window, text ="Click Me!")

#Adding the widgets,in order to the created window using the
#Keyword pack()
lblName.pack()
txtName.pack()
btnClick.pack()

# Start the event loop
window.mainloop()
