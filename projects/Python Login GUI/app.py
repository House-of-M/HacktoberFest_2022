from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class Login:
  def __init__(self, root) -> None:
    self.root = root
    self.root.title("Login UI")
    self.root.geometry("800x600+250+50")
    self.root.resizable(False, False)

    # Background image
    self.bg=ImageTk.PhotoImage(file="bkg.jpg")
    self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relheight=1, relwidth=1)

    # Login panel
    Frame_login = Frame(self.root, bg="#d6ddf4")
    Frame_login.place(x=150, y=100, width=500, height=400)

    # Titles
    title = Label(Frame_login, text="Hello there!", font=("Roboto", 18, "bold"), fg="#824bff", bg="#d6ddf4").place(x=185, y=40)
    subtitle = Label(Frame_login, text="Sign in to your account!", font=("Roboto", 14), fg="#824bff", bg="#d6ddf4").place(x=150, y=80)

    # USER INPUT:
    # username
    label_user = Label(Frame_login, text="Username", font=("Roboto", 12), fg="#2d2d2d", bg="#d6ddf4").place(x=80, y=140)
    self.username = Entry(Frame_login, font=("Roboto", 12), bg="#e6eaf7")
    self.username.place(x=80, y=170, height=35, width=350)

    # password
    label_psw = Label(Frame_login, text="Password", font=("Roboto", 12), fg="#2d2d2d", bg="#d6ddf4").place(x=80, y=220)
    self.psw = Entry(Frame_login, font=("Roboto", 12), bg="#e6eaf7")
    self.psw.place(x=80, y=250, height=35, width=350)

    # Button
    forget = Button(Frame_login, text="Forgot password ?", font=("Roboto", 10), cursor="hand2", bd=0, fg="#2d2d2d", bg="#d6ddf4").place(x=80, y=300)
    submit = Button(Frame_login, command=self.check_funct, text="Login", font=("Roboto", 12), cursor="hand2", bd=0, fg="#f2f2f2", bg="#824bff").place(x=80, y=325, height=30, width=105)

  # Functions
  def check_funct(self):
    if self.username.get()=="" or self.psw.get()=="": # if no username and/or password is filled >  gives error
      messagebox.showerror("Error", "All fields are requirend", parent=self.root)
    elif self.username.get()!="admin" or self.psw.get()!="admin123": # different from correct username and password
      messagebox.showerror("Error", "Invalid username or password.", parent=self.root)
    else:
      messagebox.showinfo("Successful login", f"Greetings {self.username.get()}!") # correct username and password


root = Tk()
obj = Login(root)
root.mainloop()
