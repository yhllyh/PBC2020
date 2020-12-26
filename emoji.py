import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb


def do():
    def happy():
        mb.showinfo("showinfo", "那真是太好了!")

    def soso():
        mb.showinfo("showinfo", "相信明天會是更好的一天")

    def sad():
        mb.showinfo("showinfo", "我可以陪你聊聊，兩個人分擔會舒服一點歐")

    def angry():
        mb.showinfo("showinfo", "就是，世上奇人異事本就多")

    def exit_program():
        root.destroy()

    root = tk.Toplevel()
    root.title("本日心情對話")
    root.geometry("425x250")
    ttk.Label(root, text="今天心情如何呢?").grid(row=0, column=1, columnspan=2)
    ttk.Button(root, text="開心(｡◕∀◕｡)", command=happy).grid(row=1, column=0)
    ttk.Button(root, text="一般般(́◉◞౪◟◉‵)", command=soso).grid(row=1, column=1)
    ttk.Button(root, text="有點小難過இдஇ", command=sad).grid(row=1, column=2)
    ttk.Button(root, text="可生氣了(╬☉д⊙)", command=angry).grid(row=1, column=3)
    ttk.Button(root, text="退出", command=exit_program).grid(
        row=2, column=1, columnspan=2, sticky=tk.E+tk.W)
    root.wait_window()
