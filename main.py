import gvar
import read_old_data
import add_new_data
import update_data_file
import timecalendar
import tkinter as tk


def homewin():
    add_new_data.do()
    update_data_file.do()


# def statwin():
#     timecalendar.do()


read_old_data.do()
print(gvar.rev)

root = tk.Tk()
root.title("Test")

menubar = tk.Menu(root)
menubar.add_command(label="主頁", command=homewin)
# menubar.add_command(label="明細", command = )
# menubar.add_command(label="統計", command=statwin)
# menubar.add_command(label="退出", command=root.quit)
root.config(menu=menubar)

root.mainloop()
