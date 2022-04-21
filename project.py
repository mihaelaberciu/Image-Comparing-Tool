from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import cv2






window = Tk()
 
window.title("Image Comparing Tool")

file = ''
file1 = ''
img1 = cv2.imread(file)
img2 = cv2.imread(file1)

def select_img1():
     global file
     file = filedialog.askopenfilename(filetypes = (("IMAGES","*.jpg"),("all files","*.*")))
def select_img2():
     global file1
     file1 = filedialog.askopenfilename(filetypes = (("IMAGES","*.jpg"),("all files","*.*")))

def imagine_adaugata():
    messagebox.showinfo('Message title', 'Message content')
    
    messagebox.showinfo('Message title', 'Message content')
def compara():
    img1 = cv2.imread(file)
    img2 = cv2.imread(file1)
    dim1 = img1.shape
    dim2 = img2.shape 
    if img1.shape == img2.shape:
        messagebox.showinfo('Related', 'Images have the same dimensions and strips')
        difference = cv2.subtract(img1, img2)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            messagebox.showinfo('Same images', 'Images are completely equal')
        else:
            messagebox.showinfo('Different images','pixel values are different')
    elif img1.shape != img2.shape:
            messagebox.showinfo("Different images", "not equal")
    
window.geometry('245x25')

window.update()

btn = Button(window,text='First Image', command=select_img1)
btn1 = Button(window,text='Second Image', command=select_img2)
btn2 = Button(window,text='Compare!', command=compara)


    


btn.grid(column=0,row=0)
btn1.grid(column=1,row=0)
btn2.grid(column=2,row=0)
 
window.mainloop()
