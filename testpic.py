import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()


def showpic():
    window = tk.Toplevel(root)
    img_open = Image.open('image.jpg')
    img_jpg = ImageTk.PhotoImage(img_open)
    label_img = tk.Label(window, image=img_jpg)
    # label_img2 = tk.Button(root, image=img_jpg)
    label_img.pack()
    window.wait_window()


is_show = tk.Button(root, text="show picture", command=showpic)
is_show.pack()
root.mainloop()
