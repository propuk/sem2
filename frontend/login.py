from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("800x533+250+110")
        self.root.resizable(False, False)
        # Background Image
        self.bg = ImageTk.PhotoImage(file="login.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        Frame_login = Frame(self.root, bg='white')
        Frame_login.place(x=200, y=140, height=300, width=450)

        title = Label(Frame_login, text="Login", font=("Imapct", 35, "bold"), fg="#d77337", bg="white").place(x=165,
                                                                                                              y=30)
        description = Label(Frame_login, text="Hostel Admin and Student Login", font=("Goudy old style", 15, "bold"),
                            fg="#d25d17", bg="white").place(x=110, y=88)
        user_lbl = Label(Frame_login, text="Username:", font=("Goudy old style", 15, "bold"),
                         fg="gray", bg="white").place(x=20, y=140)
        pass_lbl = Label(Frame_login, text="Password:", font=("Goudy old style", 15, "bold"),
                         fg="gray", bg="white").place(x=20, y=200)

        self.txt_user = Entry(Frame_login, font=("Times new roman", 15), bg="lightgray")
        self.txt_user.place(x=120, y=140, width=300, height=35)

        self.txt_pass = Entry(Frame_login, font=("Times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=120, y=200, width=300, height=35)

        reset_btn = Button(Frame_login, text="Reset Password", bd=0, bg="white", fg="#d77337",
                           font=("Times new roman", 12)).place(x=5, y=255)

        login_btn = Button(Frame_login, text="Login", fg="white", bg="#d77337",
                           font=("Imapct", 20), command=self.login_button).place(x=120, y=250, width=150, height=40)

        register_btn = Button(Frame_login, text="Register", fg="white", bg="#d77337",
                              font=("Imapct", 20), command=self.register_button).place(x=275, y=250, width=150, height=40)

    def login_button(self):
        user = self.txt_user.get()
        password = self.txt_pass.get()

        if self.txt_pass.get() == "" or self.txt_user == "":
            messagebox.showerror("Error", "Please provide your both username and password", parent=self.root)
        elif self.txt_pass.get() != "123456" or self.txt_user.get() != "Prabesh":
            messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
        else:
            messagebox.showinfo("Welcome", "Redirecting to Dashboard", parent=self.root)

    def register_button(self):
        pass

root = Tk()
obj = Login(root)
root.mainloop()
