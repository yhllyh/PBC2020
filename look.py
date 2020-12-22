import tkinter as tk

root = tk.Tk()
root.title("Test")


def savefile():
    pass


def quitfile():
    savefile()
    frame.quit


w = tk.Menubutton(root, text="Menu")
w.pack()

menubar = tk.Menu(root)
menubar.add_command(label="主頁")
menubar.add_command(label="明細")
menubar.add_command(label="統計")
menubar.add_command(label="退出", command=root.quit)
root.config(menu=menubar)


root.mainloop()
