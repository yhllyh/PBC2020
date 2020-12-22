import tkinter as tk


class Genre(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.creatwidges()

    def creatwidges(self):
        self.lblNum_f = tk.Label(self, text=' 薪資 ', bg='yellow')
        self.lblNum_c = tk.Label(self, text=' 打工 ', bg='skyblue')
        self.lblNum_l = tk.Label(self, text=' 零用 ', bg='pink')

        self.lblNum_f_01 = tk.Label(self, text=" " + '0' + " ", bg='yellow')
        self.lblNum_c_01 = tk.Label(self, text=" " + '0' + " ", bg='skyblue')
        self.lblNum_l_01 = tk.Label(self, text=" " + '0' + " ", bg='pink')

        self.lblNum_f.grid(row=0, column=0)
        self.lblNum_c.grid(row=2, column=0)
        self.lblNum_l.grid(row=4, column=0)


        self.lblNum_f_01.grid(row=0, column=2)
        self.lblNum_c_01.grid(row=2, column=2)
        self.lblNum_l_01.grid(row=4, column=2)


genre_0 = Genre()
genre_0.master.title('收入表')
genre_0.mainloop()
