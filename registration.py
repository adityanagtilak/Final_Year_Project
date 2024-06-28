import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os


window = tk.Tk()

w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
window.title("REGISTRATION FORM")
window.configure(background="grey")
#window.resizable(False,False)

Fullname = tk.StringVar()
username = tk.StringVar()
password = tk.StringVar()
password1 = tk.StringVar()

value = random.randint(1, 1000)
print(value)

# database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS registration"
               "(Fullname TEXT, username TEXT,password TEXT)")
db.commit()



def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
    fname = Fullname.get()
    un = username.get()
    pwd = password.get()
    cnpwd = password1.get()

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM registration WHERE username = ?')
    c.execute(find_user, [(username.get())])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
   
    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
    
    
    
   
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pwd == ""):
        ms.showinfo("Message", "Please Enter valid password")
   
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO registration(Fullname,username,password) VALUES(?,?,?)',
                (fname, un, pwd))
            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
            window.destroy()
            from subprocess import call
            call(["python", "login.py"])
            # window.destroy()
            

#####################################################################################################################################################

#from subprocess import call
#call(["python", "lecture_login.py"])


# assign and define variable
# def login():

# #####For background Image
image2 = Image.open('L1.jpg')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)




frame_alpr1 = tk.LabelFrame(window, text="_____________________________Registration Form____________________________", width=700, height=580, bd=5, font=('times', 14, ' bold '),bg="pink")
frame_alpr1.grid(row=0, column=5)
frame_alpr1.place(x=450, y=100)

#l1 = tk.Label(window, text="CREATE NEW ACCOUNT", font=("Times new roman", 25, "bold"), fg="white",bg="red")
#l1.place(x=600, y=20)

# that is for label1 registration

l2 = tk.Label(frame_alpr1, text="Full Name", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l2.place(x=130, y=150)
t1 = tk.Entry(frame_alpr1, textvar=Fullname, width=20, font=('', 15))
t1.place(x=330, y=150)

# that is for label 2 (full na
l4 = tk.Label(frame_alpr1, text="User Name", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l4.place(x=130, y=200)
t3 = tk.Entry(frame_alpr1, textvar=username, width=20, font=('', 15))
t3.place(x=330, y=200)

l9 = tk.Label(frame_alpr1, text="Password", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l9.place(x=130, y=250)
t9 = tk.Entry(frame_alpr1, textvar=password, width=20, font=('', 15), show="*")
t9.place(x=330, y=250)

l10 = tk.Label(frame_alpr1, text="Confirm Password", width=13, font=("Times new roman", 15, "bold"), bg="snow")
l10.place(x=130, y=300)
t10 = tk.Entry(frame_alpr1, textvar=password1, width=20, font=('', 15), show="*")
t10.place(x=330, y=300)

btn = tk.Button(frame_alpr1, text="Register", bg="black",font=("",20),fg="white", width=9, height=1, command=insert)
btn.place(x=260, y=350)
# tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
# tologin.place(x=330, y=600)
window.mainloop()