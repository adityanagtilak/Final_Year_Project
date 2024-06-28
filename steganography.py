import tkinter as tk
from tkinter import messagebox as ms
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time

#import tfModel_test as tf_test
global fn,img,img2,img3
global fn
global fn1
global fn2
global fn3

fn=""
##############################################+=============================================================
root = tk.Tk()
dt = tk.StringVar()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Multi Image steganography")


#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('2.jpeg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
# #
lbl = tk.Label(root, text="Multi Image steganography ", font=('times', 35,' bold '), height=1, width=60,bg="brown",fg="white")
lbl.place(x=0, y=0)



def en():
    from subprocess import call
    call(["python", "GUI_Master.py"])   


button1 = tk.Button(root, text="enocde ", command=en,width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button1.place(x=10, y=300)

button2 = tk.Button(root, text="decode2",width=15, command=en,height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button2.place(x=10, y=350)
root.mainloop()