"""
tinygui.py
"""


from tkinter import * # Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Ken and a GUI")

        self.label = Label(master, text="This is my first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="I am Trying!", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Adios", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Keep at it!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
