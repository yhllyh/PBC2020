import tkinter as tk


class Genre(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.creatwidges()

    def creatwidges(self):
        self.lblNum_f = tk.Label(self, text=' 食 ', bg='yellow')
        self.lblNum_c = tk.Label(self, text=' 衣 ', bg='skyblue')
        self.lblNum_l = tk.Label(self, text=' 住 ', bg='pink')
        self.lblNum_w = tk.Label(self, text=' 行 ', bg='#F8F8FF')
        self.lblNum_e = tk.Label(self, text=' 育 ', bg='#4169E1')
        self.lblNum_h = tk.Label(self, text=' 樂 ', bg='#F08080')

        self.lblNum_f_01 = tk.Label(self, text=" " + '0' + " ", bg='yellow')
        self.lblNum_c_01 = tk.Label(self, text=" " + '0' + " ", bg='skyblue')
        self.lblNum_l_01 = tk.Label(self, text=" " + '0' + " ", bg='pink')
        self.lblNum_w_01 = tk.Label(self, text=" " + '0' + " ", bg='#F8F8FF')
        self.lblNum_e_01 = tk.Label(self, text=" " + '0' + " ", bg='#4169E1')
        self.lblNum_h_01 = tk.Label(self, text=" " + '0' + " ", bg='#F08080')

        self.lblNum_f.grid(row=0, column=0)
        self.lblNum_c.grid(row=2, column=0)
        self.lblNum_l.grid(row=4, column=0)
        self.lblNum_w.grid(row=6, column=0)
        self.lblNum_e.grid(row=8, column=0)
        self.lblNum_h.grid(row=10, column=0)

        self.lblNum_f_01.grid(row=0, column=2)
        self.lblNum_c_01.grid(row=2, column=2)
        self.lblNum_l_01.grid(row=4, column=2)
        self.lblNum_w_01.grid(row=6, column=2)
        self.lblNum_e_01.grid(row=8, column=2)
        self.lblNum_h_01.grid(row=10, column=2)

genre_0 = Genre()
genre_0.master.title('支出表')
genre_0.mainloop()
