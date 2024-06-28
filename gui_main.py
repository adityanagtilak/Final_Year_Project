
import sqlite3
import tkinter  as tk 
from tkinter import * 
import time
import numpy as np

import os
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()
#root.geometry('500x500')
#root.title("Login Form")


#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Multi Image steganography")
#------------------Frame----------------------



#-------function------------------------

def reg():
    
##### tkinter window ######
    
    print("reg")
    from subprocess import call
    call(["python", "registration.py"])   



def login():
    
##### tkinter window ######
    
    print("log")
    from subprocess import call
    call(["python", "login.py"])   
    
   
        


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('pp2.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


lbl = tk.Label(root, text="Multi Image steganography ", font=('times', 40,' bold '), height=1, width=50,bg="black",fg="white")
lbl.place(x=0, y=5)


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
button1 = tk.Button(root, text='Login Now',width=20,height=3,bg='green',fg='white',command=login,font='bold').place(x=500,y=300)
button1 = tk.Button(root, text='Register',width=20,height=3,bg='green',fg='white',command=reg,font='bold').place(x=800,y=300)


root.mainloop()
