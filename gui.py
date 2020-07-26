from tkinter import *
import main

window = Tk()
window.title("IsMyPasswordSafe")
window.configure(background="black")

entered_text = ""

def click():
    entered_text =  textentry.get()
    output.delete(0.0, END)
    password_checked = main.check_password_safety(entered_text)
    output.insert(END, password_checked)



Label(window, text="Please Enter your Password", bg="black", fg="white", font="none 12 bold"). grid(row=1, column=0, sticky=W)
textentry = Entry(window, width=25, bg='white')
textentry.grid(row = 2, column=0,sticky=W)
Button(window, text="Submit", width=6, command = click) .grid(row = 3, column = 0, sticky=W)
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

window.mainloop()