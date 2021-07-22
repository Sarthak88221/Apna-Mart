from tkinter import *
from Add_Item import AddItems


#create a class of Display Category
class DisplayCategory(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.title("Display Category")
        self.geometry("1199x550+100+50")
        self.resizable(False,False)


        #Top Frame
        self.top = Frame(self, width=1199, height=180, bg="#d9c8e3")
        self.top.pack(fill=X)

        #Top Frame Design
        Label(self.top, text="Welcome to Apna Mart !!", font="times 32 bold", width=18, height=2, 
        fg="#5d0f8a", bg="#d9c8e3", bd=2).place(x=415, y=1)
        
        #  Add Button 
        self.add_items = Button(self.top, text="Add Items", font="times 14 bold", 
        width="15",height="2",bg="#594e78", fg="white",bd=0, command=self.Additems)
        self.add_items.place(x=1000, y=85)

        # Bottom Frame
        self.bottom = Frame(self, width=1199, height=370, bg="#8343ab")
        self.bottom.pack(fill=X)


    #function Add Items
    def Additems(self):
        add = AddItems()



        





        