
import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,300))
        self.master.title('Check Files')
    
        self.varBrowse1 = StringVar()
        self.varBrowse2 = StringVar()

        self.lblDisplay = Label(self.master,text='', font=("", 14))
        self.lblDisplay.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.btnBrowse1 = Button(self.master,text='Browse...', font=("", 14))
        self.btnBrowse1.grid(row=3, column=0, padx=(30,0), pady=(30,0), sticky=W)

        self.btnBrowse2 = Button(self.master,text='Browse...', font=("", 14))
        self.btnBrowse2.grid(row=4, column=0, padx=(30,0), pady=(30,0), sticky=W)

        self.txtBrowse1 = Entry(self.master,text=self.varBrowse1, font=("", 16), fg='black', bg='white')
        self.txtBrowse1.grid(row=3, column=2, padx=(30,0), pady=(30,0), sticky=W)

        self.txtBrowse2 = Entry(self.master,text=self.varBrowse2, font=("", 16), fg='black', bg='white')
        self.txtBrowse2.grid(row=4, column=2, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Check for files...", font=("", 14), command=self.submit) 
        self.btnSubmit.grid(row=6, column=0, padx=(30,0), pady=(30,0), sticky=SW)
                                 
        self.btnCancel = Button(self.master, text="Close Program", font=("", 14), command=self.cancel)
        self.btnCancel.grid(row=6, column=2, padx=(0,0), pady=(30,0), sticky=SE)

    def submit(self):
        b1 = self.Browse1.get()
        b2 = self.varBrowse2.get()
        self.lblDisplay.config(text='{}.{}'.format(b1,b2))

    def cancel(self):
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() 
    
 
