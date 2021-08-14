from tkinter import *
import tkinter.messagebox
import sqlite3

class Product:

    def __init__(self,root):

        self.root = root
        self.root.title("PROGRAMMA DI GESTIONE MAGAZZINO R21")
        self.root.geometry("1325x690")
        self.root.config(bg="yellow")

        ''' Create the frame '''
        MainFrame = Frame(self.root,bg="red")
        MainFrame.grid()

        HeadFrame = Frame(MainFrame, bd=1, padx=1, pady=10, bg='white', relief=RIDGE)
        HeadFrame.pack(side=TOP)

        self.ITitle = Label(HeadFrame, font=('arial', 50, 'bold'), fg='red',
                            text='Magazzino Inventario', bg='white')
        self.ITitle.grid()

        OperationFrame = Frame(MainFrame, bd=1, width=1300, height=60, padx=50, pady=20, bg='white', relief=RIDGE)
        OperationFrame.pack(side=BOTTOM)

    


if __name__ =='__main__':
    root=Tk()
    application = Product(root)
    root.mainloop()
