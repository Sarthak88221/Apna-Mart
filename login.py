from tkinter import *
from second_window import DisplayCategory

class login(object):
    def __init__(self,master):
        self.master =master


        # Frame
        self.left =Frame(master,height="600",width="600", bg="red")
        self.left.place(x=0,y=0)

        self.right = Frame(master,height="600",width="750", bg="white")
        self.right.place(x=600,y=0)


        # Left frame design
        # self.left_image = PhotoImage(file = '4.png')
        # self.left_image_label = Label(self.top,image = self.top_image,bg="white")
        # self.left_image_label.place(x=100,y=10)



        # Right frame design
        self.right_heading =Label(self.right,text="Log in",font="Cambria 32 bold",bg="white",fg = "black")
        self.right_heading.place(x=200,y=40)

        # icons
        self.right_login = PhotoImage(file='img/login.png')
        self.right_login_label = Label(self.right, image=self.right_login, bg="white")
        self.right_login_label.place(x=145, y=40)


        self.right_username = PhotoImage(file='img/username.png')
        self.right_username_label = Label(self.right, image=self.right_username, bg="white")
        self.right_username_label.place(x=150, y=178)


        self.right_password = PhotoImage(file='img/password.png')
        self.right_password_label = Label(self.right, image=self.right_password, bg="white")
        self.right_password_label.place(x=150, y=250)

        self.right_facebook = PhotoImage(file='img/facebook.png')
        self.right_facebook_label = Label(self.right, image=self.right_facebook, bg="white")
        self.right_facebook_label.place(x=265, y=498)

        self.right_twitter = PhotoImage(file='img/twitter.png')
        self.right_twitter_label = Label(self.right, image=self.right_twitter, bg="white")
        self.right_twitter_label.place(x=305, y=498)

        self.right_google = PhotoImage(file='img/google.png')
        self.right_google_label = Label(self.right, image=self.right_google, bg="white")
        self.right_google_label.place(x=345, y=498)

        
        self.left_img = PhotoImage(file='img/login-left.png')
        self.left_img_label = Label(self.left, image=self.left_img,bg="white")
        self.left_img_label.place(x=0, y=0)
        

        # line
        Frame(self.right,width=350,height=2,bg="#141414").place(x=155,y=215)
        Frame(self.right,width=350,height=2,bg="#141414").place(x=155,y=290)

        # input design/value
        self.entry_username = Entry(self.right,width="30",bg="white",bd=0,font="Cambria 15 bold")
        self.entry_username.insert(0,"Username")
        self.entry_username.place(x=190,y=185)

        self.entry_password = Entry(self.right,width="30",bg="white",bd=0,font="Cambria 15 bold")
        self.entry_password.insert(0,"Password")
        self.entry_password.place(x=190,y=257)

        self.right_orlogin =Label(self.right,text="Or login with",font="Cambria 13 bold",bg="white",fg = "gray63")
        # self.entry_orlogin.insert(0,"Password")
        self.right_orlogin.place(x=155,y=510)


        # login button
        self.right_button = Button(self.right, text="Log in", font="times 12 bold", width="10",height="2",bg="deep sky blue",fg="white",bd=0, command=self.login)
        self.right_button.place(x=155, y=320)
    


    # function of login Button
    def login(self):
        log = DisplayCategory()



def main():
    root=Tk()
    app= login(root)
    root.title("Apna Mart")
    root.geometry("1199x550+100+50")
    root.resizable(False,False)
    root.mainloop()

if __name__== '__main__':
 main()









