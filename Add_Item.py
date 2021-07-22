from tkinter import *


class AddItems(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.title("Display Category")
        self.geometry("1000x650+100+50")
        self.resizable(False,False)

        #top frame
        self.top = Frame(self, width=1000, height=170, bg="goldenrod")
        self.top.pack(fill=X)


        #topFrame design
        Label(self.top, text="Add New Items", font="times 28 bold", width=17, height=-2, 
        fg="black", bg="yellow", bd=2).place(x=310, y=2)
        
        



          #Bottom Frame
        self.bottom = Frame(self, width=1000, height=480, bg="#6510b5")
        self.bottom.pack(fill=X)


        #botttom frame design

        #Item name
        self.label_itemname = Label(self.bottom, text="Item Name:", font="arial 15 bold", 
        width=10, bg="#6510b5", fg="white", padx=0)
        self.label_itemname.place(x=45, y=40)
        self.entery_itemname = Entry(self.bottom, width=30, bd=6)
        self.entery_itemname.insert(0, "Enter Item Name")
        self.entery_itemname.place(x=190, y=40)

        #Price
        self.var = IntVar()
        self.label_price = Label(self.bottom, text="Price:", font="arial 15 bold", 
        width=10, bg="#6510b5", fg="white", padx=0)
        self.label_price.place(x=45, y=90)
        self.entery_price = Entry(self.bottom, width=30, bd=6, textvariable=self.var)
        
        self.entery_price.place(x=190, y=90)

        #quantity
        self.var2 = IntVar()
        self.label_quantity = Label(self.bottom, text="Quantity:", font="arial 15 bold",
        width=10, bg="#6510b5", fg="white")
        self.label_quantity.place(x=45, y=140)
        self.entery_quantity = Entry(self.bottom, width=30, bd=6, textvariable=self.var2)
        
        self.entery_quantity.place(x=190, y=140)

        #Manufactured Date
        self.label_mfd = Label(self.bottom, text="Manufactured Date:", font="arial 15 bold", 
        width=15, bg="#6510b5", fg="white", padx=0)
        self.label_mfd.place(x=45, y=190)
       # self.entery_phone = Entry(self.bottom, width=30, bd=6)
        #self.entery_phone.insert(0, "Enter phone Number")
        #self.entery_phone.place(x=190, y=190)

        #Expiry Date
        self.label_expd = Label(self.bottom, text="Expiry Date:", font="arial 15 bold",
         width=15, bg="#6510b5", fg="white", padx=0)
        self.label_expd.place(x=45, y=240)

        #self.entery_address = Text(self.bottom, width=28, bd=6, height=5)
        #self.entery_address.place(x=190, y=240)

        #button
        self.button = Button(self.bottom, text="Add Items", 
        font="arial 12 bold", width=15, fg="#160163", bg="white")
        self.button.place(x=120, y=350)
