import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import numpy as np
import time
import click
from PIL import Image, ImageTk

global fn,fn1,input1, img, img1, img2

fn=""
fn1=""

##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Main Page")


#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('2.jpeg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)



   
    
   
    
   
    
    
lbl = tk.Label(root, text="Image Stegnography System ", font=('times', 35,' bold '), height=1, width=60,bg="brown",fg="white")
lbl.place(x=0, y=0)

class Steganography:

    @staticmethod
    def __int_to_bin(rgb):
        """Convert an integer tuple to a binary (string) tuple.

        :param rgb: An integer tuple (e.g. (220, 110, 96))
        :return: A string tuple (e.g. ("00101010", "11101011", "00010110"))
        """
        r, g, b = rgb
        return (f'{r:08b}',
                f'{g:08b}',
                f'{b:08b}')

    @staticmethod
    def __bin_to_int(rgb):
        """Convert a binary (string) tuple to an integer tuple.

        :param rgb: A string tuple (e.g. ("00101010", "11101011", "00010110"))
        :return: Return an int tuple (e.g. (220, 110, 96))
        """
        r, g, b = rgb
        return (int(r, 2),
                int(g, 2),
                int(b, 2))

    @staticmethod
    def __merge_rgb(rgb1, rgb2):
        """Merge two RGB tuples.

        :param rgb1: A string tuple (e.g. ("00101010", "11101011", "00010110"))
        :param rgb2: Another string tuple
        (e.g. ("00101010", "11101011", "00010110"))
        :return: An integer tuple with the two RGB values merged.
        """
        r1, g1, b1 = rgb1
        r2, g2, b2 = rgb2
        rgb = (r1[:4] + r2[:4],
               g1[:4] + g2[:4],
               b1[:4] + b2[:4])
        return rgb

    @staticmethod
    def merge(img1, img2):
        print(3)
        """Merge two images. The second one will be merged into the first one.

        :param img1: First image
        :param img2: Second image
        :return: A new merged image.
        """

        # Check the images dimensions
        if img2.size[0] > img1.size[0] or img2.size[1] > img1.size[1]:
            raise ValueError('Image 2 should not be larger than Image 1!')

        # Get the pixel map of the two images
        pixel_map1 = img1.load()
        pixel_map2 = img2.load()

        # Create a new image that will be outputted
        new_image = Image.new(img1.mode, img1.size)
        pixels_new = new_image.load()

        for i in range(img1.size[0]):
            for j in range(img1.size[1]):
                rgb1 = Steganography.__int_to_bin(pixel_map1[i, j])

                # Use a black pixel as default
                rgb2 = Steganography.__int_to_bin((0, 0, 0))

                # Check if the pixel map position is valid for the second image
                if i < img2.size[0] and j < img2.size[1]:
                    rgb2 = Steganography.__int_to_bin(pixel_map2[i, j])

                # Merge the two pixels and convert it to a integer tuple
                rgb = Steganography.__merge_rgb(rgb1, rgb2)

                pixels_new[i, j] = Steganography.__bin_to_int(rgb)

        return new_image

    @staticmethod
    def unmerge(img):
        """Unmerge an image.

        :param img: The input image.
        :return: The unmerged/extracted image.
        """

        # Load the pixel map
        pixel_map = img.load()

        # Create the new image and load the pixel map
        new_image = Image.new(img.mode, img.size)
        pixels_new = new_image.load()

        # Tuple used to store the image original size
        original_size = img.size

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                # Get the RGB (as a string tuple) from the current pixel
                r, g, b = Steganography.__int_to_bin(pixel_map[i, j])

                # Extract the last 4 bits (corresponding to the hidden image)
                # Concatenate 4 zero bits because we are working with 8 bit
                rgb = (r[4:] + '0000',
                       g[4:] + '0000',
                       b[4:] + '0000')

                # Convert it to an integer tuple
                pixels_new[i, j] = Steganography.__bin_to_int(rgb)

                # If this is a 'valid' position, store it
                # as the last valid position
                if pixels_new[i, j] != (0, 0, 0):
                    original_size = (i + 1, j + 1)

        # Crop the image based on the 'valid' pixels
        new_image = new_image.crop((0, 0, original_size[0], original_size[1]))

        return new_image
    
    def submit(fn, fn1):
   # global fn, fn1
    
    
        input1 = Image.open(fn)
        
        img = Image.open(fn1)
    
        
        img1 = input1
        
        img2 = img
        
        #this is the path where we will save the encoded Image.
        output = ".\encode.png"
    
        merged_image = Steganography.merge(Image.open(img1), Image.open(img2))
        merged_image.save(output)
        print(1)    
    
    def input1():
        ##Input 1 image
        global fn
        fn=""
        
        
        fileName = askopenfilename(initialdir='/dataset/images/', title='Select image for Aanalysis ', filetypes=[("all files", "*.*")])
        IMAGE_SIZE=300
        imgpath = fileName
        fn = fileName
        
        input1 = Image.open(imgpath)
        input1 = input1.resize((IMAGE_SIZE,IMAGE_SIZE))
        input1 = np.array(input1)
    
    
    
        x1 = int(input1.shape[0])
        y1 = int(input1.shape[1])
    
        input1 = Image.fromarray(input1)
        input1 = ImageTk.PhotoImage(image=input1)
        input1 = tk.Label(root, image=input1, height=250, width=250)
        
        
        input1.image = input1
        input1.place(x=300, y=100)
        
        
    
   
    ########################### ENCODE CODE ##################################
    
    # ##HIDE  IMAGE
    def hide():
        global fn1
    
        
        fn1=""
        
        fileName = askopenfilename(initialdir='D:/Python-Project-2022/steganography-main/steganography-main/dataset/images', title='Select image for Aanalysis ',
                                   filetypes=[("all files", "*.*")])
        IMAGE_SIZE=300
        imgpath = fileName
        fn1 = fileName
    
        img = Image.open(imgpath)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
    
    
    
        x1 = int(img.shape[0])
        y1 = int(img.shape[1])
    
    
    
        im = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=im)
        img = tk.Label(root, image=imgtk, height=250, width=250)
        
        img.image = imgtk
        img.place(x=300, y=100)
        
        #hide
   
        
    button1 = tk.Button(root, text=" Select_Image ",command = input1,width=15, height=1, font=('times', 15, ' bold '),bg="red",fg="black")
    button1.place(x=10, y=100)
     
     
    button2 = tk.Button(root, text="Hide",command=hide, width=15, height=1, font=('times', 15, ' bold '),bg="red",fg="black")
    button2.place(x=10, y=150)
    
    
    
    button2 = tk.Button(root, text="Submit",command=submit, width=15, height=1, font=('times', 15, ' bold '),bg="red",fg="black")
    button2.place(x=10, y=200)
    #Hide1 images
    # def hide1():
    #     fileName = askopenfilename(initialdir='D:/Python-Project-2022/steganography-main/steganography-main/dataset/images', title='Select image for Aanalysis ',
    #                                filetypes=[("all files", "*.*")])
    #     IMAGE_SIZE=300
    #     imgpath = fileName
    #     fn = fileName
    
    
    # #        img = Image.open(imgpath).convert("L")
    #     img1 = Image.open(imgpath)
    #     img1 = img1.resize((IMAGE_SIZE,IMAGE_SIZE))
    #     img1 = np.array(img1)
    
    
    
    #     x1 = int(img1.shape[0])
    #     y1 = int(img1.shape[1])
    
    #     img1 = Image.fromarray(img1)
    #     img1 = ImageTk.PhotoImage(image=img1)
    #     img1 = tk.Label(root, image=img1, height=250, width=250)
        
    #     img1.image = img1
    #     img1.place(x=300, y=100)
        
    #     img3 = ".\encode.png"
    #     img4 = img1
    #     #this is the path where we will save the encoded Image.
    #     output1 = ".\encode1.png"
    
    #     merged_image = Steganography.merge(Image.open(img3), Image.open(img4))
    #     merged_image.save(output1)
    #     print(2)
        
    # def hide2():
    # ###Hide2
    
    #     fileName = askopenfilename(initialdir='D:/Python-Project-2022/steganography-main/steganography-main/dataset/images', title='Select image for Aanalysis ',
    #                                filetypes=[("all files", "*.*")])
    #     IMAGE_SIZE=300
    #     imgpath = fileName
    #     fn = fileName
    
    
    # #        img = Image.open(imgpath).convert("L")
    #     img2 = Image.open(imgpath)
    #     img2 = img2.resize((IMAGE_SIZE,IMAGE_SIZE))
    #     img2 = np.array(img2)
    
    
    
    #     x1 = int(img2.shape[0])
    #     y1 = int(img2.shape[1])
    
    
    #     img2 = Image.fromarray(img2)
    #     img2 = ImageTk.PhotoImage(image=img2)
    #     img2 = tk.Label(root, image=img2, height=250, width=250)
        
    #     img2.image = img2
    #     img2.place(x=300, y=100)
        
    #     img5 =  ".\encode1.png"
    #     img6 = img2
    #     #this is the path where we will save the encoded Image.
    #     output2 = ".\encode2.png"
    
    #     merged_image = Steganography.merge(Image.open(img5), Image.open(img6))
    #     merged_image.save(output2)
    #     print(4) 
        
    
    # #################  DECODE CODE #############################
    
    # img7 = ".\encode2.png"
    # decode2 = ".\decode2.png"
    # unmerged_image = Steganography.unmerge(Image.open(img7))
    # unmerged_image.save(decode2)
    # print(5)
    
    # img8 = ".\encode1.png"
    # decode3 = ".\decode3.png"
    # unmerged_image = Steganography.unmerge(Image.open(img8))
    # unmerged_image.save(decode3)
    # print(6)
    
    # img9 = ".\encode.png"
    # decode = ".\decode.png"
    # unmerged_image = Steganography.unmerge(Image.open(img9))
    # unmerged_image.save(decode)
    # print(5)


#        out_label.config(text=imgpath)


# @cli.command()
# @click.option('--img', required=True, type=str, help='Image that will be hidden')
# @click.option('--output', required=True, type=str, help='Output image')
# def unmerge(img, output):
#     unmerged_image = Steganography.unmerge(Image.open(img))
#     unmerged_image.save(output)


# if __name__ == '__main__':
    
#     main()    
    
def window():
    root.destroy()




# button1 = tk.Button(root, text=" Select_Image ",command = openimage1,width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button1.place(x=10, y=50)

# button2 = tk.Button(root, text="Hide",command=hide, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button2.place(x=10, y=100)

# button3 = tk.Button(root, text="Hide1", command = hide1, width=12, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button3.place(x=10, y=150)

# button4 = tk.Button(root, text="Hide2", command = hide2, width=15, height=1,bg="white",fg="black", font=('times', 15, ' bold '))
# button4.place(x=10, y=200)
#
#
#button5 = tk.Button(frame_alpr, text="button5", command=window,width=8, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
#button5.place(x=450, y=20)


# exit = tk.Button(root, text="Encode", command=main, width=15, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
# exit.place(x=10, y=260)



root.mainloop()