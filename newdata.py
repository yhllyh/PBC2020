import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
window = tk.Tk()

window.title('記帳小幫手')
window.geometry('800x600')
window.configure(background='pink')

header_label = tk.Label(window, text='記帳小幫手')
header_label.pack()

#  支出/收入、日期、類別、金額

#  以下為支出/收入下拉式選單的部分
nopt = tk.StringVar()
options = ('收入', '支出')
option = ttk.Combobox(window, width=30, textvariable=nopt, values=options)
option.pack(side=tk.TOP)

#  以下為使用者輸入日期的部分
ndate = tk.StringVar()
date_frame = tk.Frame(window)
date_frame.pack(side=tk.TOP)
date_label = tk.Label(date_frame, text='日期：(xxxx/xx/xx)')
date_label.pack(side=tk.LEFT)
date_entry = tk.Entry(date_frame, textvariable=ndate)
date_entry.pack(side=tk.LEFT)

#  以下為類別下拉式選單的部分
ncat = tk.StringVar()
categories = ('食', '衣', '住', '行', '育', '樂', '醫療', '薪資', '打工', '零用')
category = ttk.Combobox(window, width=30, textvariable=ncat, values=categories)
category.pack(side=tk.TOP)

#  以下為金額的部分
nmoney = tk.StringVar()
money_frame = tk.Frame(window)
money_frame.pack(side=tk.TOP)
money_label = tk.Label(money_frame, text='金額：(NTD)')
money_label.pack(side=tk.LEFT)
money_entry = tk.Entry(money_frame, textvariable=nmoney)
money_entry.pack(side=tk.LEFT)


def getdata():
    cur_opt = option.get()
    cur_date = ndate.get()
    cur_cat = ncat.get()
    cur_money = nmoney.get()
    line = cur_opt + " " + cur_date + " " + cur_cat + " " + cur_money
    messagebox.showinfo("已新增", line)
    # print(cur_opt, cur_date, cur_cat, cur_money)


press = tk.Button(window, text="新增", command=getdata)
press.pack()

window.mainloop()
