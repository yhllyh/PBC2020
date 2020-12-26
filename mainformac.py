import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import time
import datetime
# import func


"""def homewin():
    add_new_data.do()
    update_data_file.do()


def statwin():
    timebug.do()"""

rev = []
exp = []
with open(file='data.txt', mode='r', encoding='utf-8') as f:
    change = False
    for line in f:
        line = line.strip()
        if line == "ExpEnd" or line == "RevEnd":
            change = not change
            continue
        line = line.split()
        if change:
            rev.append(line)
        else:
            exp.append(line)

window = tk.Tk()
window.title("Test")

menubar = tk.Menu(window)
# menubar.add_command(label="主頁", command=homewin)
# menubar.add_command(label="明細", command = )
menubar.add_command(label="統計", command=window.quit)
menubar.add_command(label="退出", command=window.quit)
window.config(menu=menubar)
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
category = ttk.Combobox(
    window, width=30, textvariable=ncat, values=categories)
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
    line = [cur_opt, cur_date, cur_cat, cur_money]
    if(cur_opt == "收入"):
        pos = func.bisearch(rev, line)
        rev.insert(pos, line)
    elif(cur_opt == "支出"):
        pos = func.bisearch(exp, line)
        exp.insert(pos, line)
    else:
        messagebox.showinfo("輸入錯誤", "數值錯誤")
    # messagebox.showinfo("已新增", line)
    # print(cur_opt, cur_date, cur_cat, cur_money)
    try:
        f = open(file="data.txt", mode='w', encoding='utf-8')
        for item in exp:
            line = " ".join(item)
            f.write(line + "\n")
        f.write("ExpEnd\n")
        for item in rev:
            line = " ".join(item)
            f.write(line + "\n")
        f.write("RevEnd\n")
    finally:
        f.close()


press = tk.Button(window, text="新增", command=getdata)
press.pack()

window.mainloop()

# root.mainloop()
