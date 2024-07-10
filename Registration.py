import tkinter as tk
from tkinter import messagebox as ms
import warnings
warnings.filterwarnings('ignore') # suppress import warnings
import sqlite3
import re
from PIL import Image , ImageTk 


window =tk.Tk()
window.resizable(0, 0)

window.geometry("520x650+350+0")
window.title("REGISTRATION FORM")

#####For background Image
image2 =Image.open("bglogin.jpg")
image2 =image2.resize((520,650), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)



Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var =tk.IntVar()
age = tk.IntVar()
password =tk.StringVar()
password1=tk.StringVar()
#database code
db = sqlite3.connect('USER.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS entry"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
db.commit()


def insert():

    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd=password1.get()

    with sqlite3.connect('USER.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM entry WHERE username = ?')
    c.execute(find_user, [(username.get())])

    #else:
     #   ms.showinfo('Success!', 'Account Created Successfully !')

    #to check mail
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex, email)):
        a=True
    else:
        a=False
    #validation
    if(fname.isdigit()or(fname=="")):
        ms.showinfo("Message","please enter valid name")
    elif(addr==""):
        ms.showinfo("Message","Please Enter Address")
    elif(email=="")or(a==False):
        ms.showinfo("Message", "Please Enter valid email")
    elif((mobile)<1000000000):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif((time>100)or(time==0)):
        ms.showinfo("Message", "Please Enter valid age")
    elif(c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif(pwd==""):
        ms.showinfo("Message", "Please Enter valid password")
    elif(var==False):
        ms.showinfo("Message", "Please Enter gender")
    elif(pwd!=cnpwd):
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('USER.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO entry(Fullname, address, username, Email, Phoneno, Gender, age , password) VALUES(?,?,?,?,?,?,?,?)',
                       (fname, addr,un, email, mobile, gender, time, pwd))
            db.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
            window.destroy()
#            from subprocess import call
#            call(["python","Login.py"])

    
   
l1=tk.Label(window,text="Registration Form",font=("Times new roman", 20, "bold"),bg="light cyan2",fg="black")
l1.place(x=180, y=15)

#that is for label1 registration

l2 =tk.Label(window, text="Full Name :", width=12,font=("Times new roman", 15, "bold"),bg="light cyan2")
l2.place(x=60, y=80)
t1 =tk.Entry(window, textvar=Fullname,width=20, font=('', 15))
t1.place(x=230, y=80)
# that is for label 2 (full name)


l3 =tk.Label(window, text="Address :", width=12,font=("Times new roman", 15, "bold"),bg="light cyan2")
l3.place(x=60, y=150)
t2 =tk.Entry(window, textvar=address,width=20, font=('', 15))
t2.place(x=230, y=150)
#that is for label 3(address)



l5 =tk.Label(window, text="E-mail :", width=12,font=("Times new roman", 15, "bold"),bg="light cyan2")
l5.place(x=60, y=200)
t4 =tk.Entry(window, textvar=Email,width=20, font=('', 15))
t4.place(x=230, y=200)
#that is for email address

l6 =tk.Label(window, text="Phone number :", width=12,font=("Times new roman", 15, "bold"),bg="light cyan2")
l6.place(x=60, y=250)
t5 =tk.Entry(window, textvar= Phoneno,width=20, font=('', 15))
t5.place(x=230, y=250)
#phone number
l7 =tk.Label(window, text="Gender :", width=12,font=("Times new roman", 15, "bold"),bg="light cyan2")
l7.place(x=60, y=300)
#gender
tk.Radiobutton(window, text="Male", padx=5,width=5,bg="light cyan2", font=("bold", 15), variable=var, value=1).place(x=230, y=300)
tk.Radiobutton(window, text="Female", padx=20,width=5,bg="light cyan2", font=("bold", 15), variable=var, value=2).place(x=230, y=350)


l8 =tk.Label(window, text="Age :", width=12, font=("Times new roman", 15, "bold"),bg="light cyan2")
l8.place(x=60, y=400)
t6 =tk.Entry(window, textvar=age,width=20, font=('', 15))
t6.place(x=230, y=400)

l4 =tk.Label(window, text="User Name :", width=12,font=("Times new roman", 15, "bold"),bg="light cyan2")
l4.place(x=60, y=450)
t3 =tk.Entry(window, textvar=username,width=20, font=('', 15))
t3.place(x=230, y=450)

l9 =tk.Label(window, text="Password :", width=12, font=("Times new roman", 15, "bold"),bg="light cyan2")
l9.place(x=60, y=500)
t9 =tk.Entry(window, textvar=password,width=20, font=('', 15),show="*")
t9.place(x=230, y=500)

l10 =tk.Label(window, text="Confirm Password:", width=13, font=("Times new roman", 15, "bold"),bg="light cyan2")
l10.place(x=60, y=550)
t10 =tk.Entry(window, textvar=password1,width=20, font=('', 15),show="*")
t10.place(x=230, y=550)

btn=tk.Button(window, text="Register", bg ="black",width=10, fg = "white", font=("Times new roman", 15, "bold"), command=insert)
btn.place(x=200, y=600)

window.mainloop()