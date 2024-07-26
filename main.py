import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief

root = Tk()
root.title("Image Color Detection Software")
root.geometry("800x470+100+100")
root.configure(bg="#e4e8eb")
root.resizable(False, False)


def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select Image File",
                                          filetypes=(('PNG file', '*.png'),
                                                     ("JPG file", '*.jpg'),
                                                     ("All files", '*.*')))
    if filename:
        img = Image.open(filename)
        img = img.resize((310, 270), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img, width=310, height=270)
        lbl.image = img


def FindColor():
    if not filename:
        return

    ct = ColorThief(filename)
    palette = ct.get_palette(color_count=10)

    color_hex = [f"#{c[0]:02x}{c[1]:02x}{c[2]:02x}" for c in palette]

    colors.itemconfig(id1, fill=color_hex[0])
    colors.itemconfig(id2, fill=color_hex[1])
    colors.itemconfig(id3, fill=color_hex[2])
    colors.itemconfig(id4, fill=color_hex[3])
    colors.itemconfig(id5, fill=color_hex[4])
    colors2.itemconfig(id6, fill=color_hex[5])
    colors2.itemconfig(id7, fill=color_hex[6])
    colors2.itemconfig(id8, fill=color_hex[7])
    colors2.itemconfig(id9, fill=color_hex[8])
    colors2.itemconfig(id10, fill=color_hex[9])

    hex_labels = [hex1, hex2, hex3, hex4, hex5, hex6, hex7, hex8, hex9, hex10]
    for i in range(10):
        hex_labels[i].configure(text=color_hex[i])


filename = ""

# icon
image_icon = PhotoImage(file="images/icon.png")
root.iconphoto(False, image_icon)

Label(root, width=120, height=10, bg="#4272f9").pack()

# frame
frame = Frame(root, width=700, height=370, bg="#fff")
frame.place(x=50, y=50)

# open and resize logo
logo_path = "images/color_circle 2.png"
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((70, 70), Image.LANCZOS)
logo = ImageTk.PhotoImage(logo_image)

Label(frame, image=logo, bg="#fff").place(x=10, y=10)
Label(frame, text="Color Finder", font="arial 25 bold", bg="white", fg='black').place(x=100, y=20)

# color1
colors = Canvas(frame, bg='#fff', width=150, height=265, bd=0)
colors.place(x=20, y=90)

id1 = colors.create_rectangle((10, 10, 50, 50), fill="#b8255f")
id2 = colors.create_rectangle((10, 50, 50, 100), fill="#db4035")
id3 = colors.create_rectangle((10, 100, 50, 150), fill="#ff9933")
id4 = colors.create_rectangle((10, 150, 50, 200), fill="#fad000")
id5 = colors.create_rectangle((10, 200, 50, 250), fill="#afb83b")

hex1 = Label(colors, text="#b8255f", fg="#000", font="arial 14 bold", bg="white")
hex1.place(x=60, y=15)

hex2 = Label(colors, text="#db4035", fg="#000", font="arial 14 bold", bg="white")
hex2.place(x=60, y=65)

hex3 = Label(colors, text="#ff9933", fg="#000", font="arial 14 bold", bg="white")
hex3.place(x=60, y=115)

hex4 = Label(colors, text="#fad000", fg="#000", font="arial 14 bold", bg="white")
hex4.place(x=60, y=165)

hex5 = Label(colors, text="#afb83b", fg="#000", font="arial 14 bold", bg="white")
hex5.place(x=60, y=215)

# color2
colors2 = Canvas(frame, bg='#fff', width=150, height=265, bd=0)
colors2.place(x=180, y=90)

id6 = colors2.create_rectangle((10, 10, 50, 50), fill="#7ecc49")
id7 = colors2.create_rectangle((10, 50, 50, 100), fill="#299438")
id8 = colors2.create_rectangle((10, 100, 50, 150), fill="#6accbc")
id9 = colors2.create_rectangle((10, 150, 50, 200), fill="#158fad")
id10 = colors2.create_rectangle((10, 200, 50, 250), fill="#14aaf5")

hex6 = Label(colors2, text="#7ecc49", fg="#000", font="arial 14 bold", bg="white")
hex6.place(x=60, y=15)

hex7 = Label(colors2, text="#299438", fg="#000", font="arial 14 bold", bg="white")
hex7.place(x=60, y=65)

hex8 = Label(colors2, text="#6accbc", fg="#000", font="arial 14 bold", bg="white")
hex8.place(x=60, y=115)

hex9 = Label(colors2, text="#158fad", fg="#000", font="arial 14 bold", bg="white")
hex9.place(x=60, y=165)

hex10 = Label(colors2, text="#14aaf5", fg="#000", font="arial 14 bold", bg="white")
hex10.place(x=60, y=215)

# select image
selectimage = Frame(frame, width=340, height=350, bg="#d6dee5")
selectimage.place(x=350, y=10)

f = Frame(selectimage, bd=3, bg="black", width=320, height=280, relief=GROOVE)
f.place(x=10, y=10)

lbl = Label(f, bg="black")
lbl.place(x=0, y=0)

Button(selectimage, text="Select Image", width=12, height=1, font="arial 14 bold", command=showimage).place(x=10, y=300)
Button(selectimage, text="Find Colors", width=12, height=1, font="arial 14 bold", command=FindColor).place(x=176, y=300)

root.mainloop()
