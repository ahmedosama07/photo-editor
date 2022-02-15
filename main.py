# import required modules
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from turtle import width
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os
# contrast border thumbnail 
root = Tk()
root.title("Not Photoshop")
root.geometry("1024x800")
root.resizable(False, False)

def selected():
    global img_path, img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd()) 
    img = Image.open(img_path)
    img.thumbnail((950, 600))
    img1 = ImageTk.PhotoImage(img)
    canvas2.create_image(500, 300, image=img1)
    canvas2.image=img1




def blur(event):
    global img_path, img1, imgg
    for m in range(0, v1.get()+1):
            img = Image.open(img_path)
            img.thumbnail((950, 600))
            imgg = img.filter(ImageFilter.BoxBlur(m))
            img1 = ImageTk.PhotoImage(imgg) 
            canvas2.create_image(500, 300, image=img1)
            canvas2.image=img1



def brightness(event):
    global img_path, img2, img3
    for m in range(0, v2.get()+1):
            img = Image.open(img_path)
            img.thumbnail((950, 600))
            imgg = ImageEnhance.Brightness(img)
            img2 = imgg.enhance(m)
            img3 = ImageTk.PhotoImage(img2)
            canvas2.create_image(500, 300, image=img3)
            canvas2.image=img3



def contrast(event):
    global img_path, img4, img5
    for m in range(0, v3.get()+1):
            img = Image.open(img_path)
            img.thumbnail((950, 600))
            imgg = ImageEnhance.Contrast(img)
            img4 = imgg.enhance(m)
            img5 = ImageTk.PhotoImage(img4)
            canvas2.create_image(500, 300, image=img5)
            canvas2.image=img5


def rotate_image(event):
        global img_path, img6, img7
        img = Image.open(img_path)
        img.thumbnail((950, 600))
        img6 = img.rotate(int(rotate_combo.get()))
        img7 = ImageTk.PhotoImage(img6)
        canvas2.create_image(500, 300, image=img7)
        canvas2.image=img7
        


def flip_image(event):
        global img_path, img8, img9
        img = Image.open(img_path)
        img.thumbnail((950, 600))
        if flip_combo.get() == "FLIP LEFT TO RIGHT":
            img8 = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif flip_combo.get() == "FLIP TOP TO BOTTOM":
            img8 = img.transpose(Image.FLIP_TOP_BOTTOM)
        img9 = ImageTk.PhotoImage(img8)
        canvas2.create_image(500, 300, image=img9)
        canvas2.image=img9   




img1 = None
img3 = None
img5 = None
img7 = None
img9 = None
img11 = None



def save():
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9
    #file=None
    ext = img_path.split(".")[-1]
    file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
    if file: 
            if canvas2.image==img1:
                imgg.save(file)
            elif canvas2.image==img3:
                img2.save(file)
            elif canvas2.image==img5:
                img4.save(file)
            elif canvas2.image==img7:
                img6.save(file)
            elif canvas2.image==img9:
                img8.save(file)




# create labels, scales and comboboxes
blurr = Label(root, text="Blur:", font=("ariel 17 bold"), width=9, anchor='e')
blurr.place(x=15, y=8)
v1 = IntVar()
scale1 = ttk.Scale(root, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=blur) 
scale1.place(x=150, y=10)
bright = Label(root, text="Brightness:", font=("ariel 17 bold"))
bright.place(x=8, y=50)
v2 = IntVar()   
scale2 = ttk.Scale(root, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=brightness) 
scale2.place(x=150, y=55)
contrast = Label(root, text="Contrast:", font=("ariel 17 bold"))
contrast.place(x=35, y=92)
v3 = IntVar()   
scale3 = ttk.Scale(root, from_=0, to=10, variable=v3, orient=HORIZONTAL, command=contrast) 
scale3.place(x=150, y=100)
rotate = Label(root, text="Rotate:", font=("ariel 17 bold"))
rotate.place(x=370, y=8)
values = [0, 90, 180, 270, 360]
rotate_combo = ttk.Combobox(root, values=values, font=('ariel 10 bold'))
rotate_combo.place(x=460, y=15)
rotate_combo.bind("<<ComboboxSelected>>", rotate_image)
flip = Label(root, text="Flip:", font=("ariel 17 bold"))
flip.place(x=400, y=50)
values1 = ["FLIP LEFT TO RIGHT", "FLIP TOP TO BOTTOM"]
flip_combo = ttk.Combobox(root, values=values1, font=('ariel 10 bold'))
flip_combo.place(x=460, y=57)
flip_combo.bind("<<ComboboxSelected>>", flip_image)


# create canvas to display image
canvas2 = Canvas(root, width="1010", height="600", relief=RIDGE, bd=2)
canvas2.place(x=0, y=150)


# create buttons
btn1 = Button(root, text="Select Image", width=12, bg='black', fg='gold', font=('ariel 12 bold'), relief=GROOVE, command=selected)
btn1.place(x=800, y=15)
btn2 = Button(root, text="Save", width=12, bg='green', fg='gold', font=('ariel 12 bold'), relief=GROOVE, command=save)
btn2.place(x=800, y=55)
btn3 = Button(root, text="Exit", width=12, bg='red', fg='gold', font=('ariel 12 bold'), relief=GROOVE, command=root.destroy)
btn3.place(x=800, y=92)
root.mainloop()