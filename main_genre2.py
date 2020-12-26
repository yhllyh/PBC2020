"""引用各種套件"""
import emoji
import func
import update_data_file
import add_new_data
import read_old_data
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import gvar
import time
import datetime
from PIL import Image, ImageTk
from tkinter import ttk  # 匯入內部包
import calendar
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import datetime as r_datetime
import time as r_time
import matplotlib.pyplot as plt
import numpy as np
"""引入其他檔案"""
datetime = calendar.datetime.datetime
timedelta = calendar.datetime.timedelta
st_date = "2020-12-25"
ed_date = "2020-12-25"
food_exp = 0  # 食
clothing_exp = 0  # 衣
living_exp = 0  # 住
trans_exp = 0  # 行
learning_exp = 0  # 育
entertainment_exp = 0  # 樂
medical_exp = 0  # 醫療

salary = 0  # 薪資
wage = 0  # 打工
allowance = 0  # 零用

"""統計部分"""
"""擷取時間段"""


def timecalendar():
    """用日曆選擇想要查的時間段"""
    def showcatog():
        genre_0 = tk.Toplevel()
        genre_0.title('按類別統計')
        global food_exp, clothing_exp, living_exp, trans_exp, learning_exp, entertainment_exp, medical_exp
        global salary, wage, allowance
        # print(salary)
        lblNum_r1 = tk.Label(genre_0, text=' 薪資   ' +
                             str(salary), bg='yellow')
        lblNum_r2 = tk.Label(genre_0, text=' 打工   ' +
                             str(wage), bg='skyblue')
        lblNum_r3 = tk.Label(genre_0, text=' 零用   ' +
                             str(allowance), bg='pink')
        lblNum_r1.pack()
        lblNum_r2.pack()
        lblNum_r3.pack()
        lblNum_e1 = tk.Label(genre_0, text=' 食   ' +
                             str(food_exp), bg='yellow')
        lblNum_e2 = tk.Label(genre_0, text=' 衣   ' +
                             str(clothing_exp), bg='skyblue')
        lblNum_e3 = tk.Label(genre_0, text=' 住   ' +
                             str(living_exp), bg='pink')
        lblNum_e4 = tk.Label(genre_0, text=' 行   ' +
                             str(trans_exp), bg='#F8F8FF')
        lblNum_e5 = tk.Label(genre_0, text=' 育   ' +
                             str(learning_exp), bg='#4169E1')
        lblNum_e6 = tk.Label(genre_0, text=' 樂   ' +
                             str(entertainment_exp), bg='#F08080')
        lblNum_e1.pack()
        lblNum_e2.pack()
        lblNum_e3.pack()
        lblNum_e4.pack()
        lblNum_e5.pack()
        lblNum_e6.pack()

        genre_0.wait_window()

    def showpic():
        win = tk.Toplevel()
        win.title("win")
        exp_open = Image.open('exp_donut.jpg')
        rev_open = Image.open('rev_donut.jpg')
        exp_open.thumbnail((650, 650))
        rev_open.thumbnail((650, 650))
        exp_jpg = ImageTk.PhotoImage(exp_open)
        rev_jpg = ImageTk.PhotoImage(rev_open)
        # exp_jpg.resize("500x100")
        label_exp = tk.Label(win, image=exp_jpg)
        label_rev = tk.Label(win, image=rev_jpg)
        label_exp.pack(side=tk.LEFT)
        label_rev.pack(side=tk.RIGHT)
        win.wait_window()

    class Calendar:
        def __init__(s, point=None):
            s.master = tk.Toplevel()
            s.master.withdraw()
            s.master.attributes('-topmost', True)
            fwday = calendar.SUNDAY
            year = datetime.now().year
            month = datetime.now().month
            locale = None
            sel_bg = '#ecffc4'
            sel_fg = '#05640e'
            s._date = datetime(year, month, 1)  # 每月第一日
            s._selection = None  # 設置為未選中日期
            s.G_Frame = ttk.Frame(s.master)
            s._cal = s.__get_calendar(locale, fwday)
            s.__setup_styles()        # 創建自定義樣式
            s.__place_widgets()       # pack/grid 小部件
            s.__config_calendar()     # 調整日歷列和安裝標記
            # 配置畫布和正確的綁定，以選擇日期。
            s.__setup_selection(sel_bg, sel_fg)
            # 存儲項ID，用於稍後插入。
            s._items = [s._calendar.insert(
                '', 'end', values='') for _ in range(6)]
            # 在當前空日歷中插入日期
            s._update()
            s.G_Frame.pack(expand=1, fill='both')
            s.master.overrideredirect(1)
            s.master.update_idletasks()
            width, height = s.master.winfo_reqwidth(), s.master.winfo_reqheight()
            s.height = height
            if point:
                x, y = point[0], point[1]
            else:
                x, y = (s.master.winfo_screenwidth() - width) / \
                    2, (s.master.winfo_screenheight() - height)/2
            s.master.geometry('%dx%d+%d+%d' % (width, height, x, y))  # 窗口位置居中
            s.master.after(300, s._main_judge)
            s.master.deiconify()
            s.master.focus_set()
            s.master.wait_window()  # 這裡應該使用wait_window掛起窗口，如果使用mainloop,可能會導致主程序很多錯誤

        def __get_calendar(s, locale, fwday):
            if locale is None:
                return calendar.TextCalendar(fwday)
            else:
                return calendar.LocaleTextCalendar(fwday, locale)

        def __setitem__(s, item, value):
            if item in ('year', 'month'):
                raise AttributeError("attribute '%s' is not writeable" % item)
            elif item == 'selectbackground':
                s._canvas['background'] = value
            elif item == 'selectforeground':
                s._canvas.itemconfigure(s._canvas.text, item=value)
            else:
                s.G_Frame.__setitem__(s, item, value)

        def __getitem__(s, item):
            if item in ('year', 'month'):
                return getattr(s._date, item)
            elif item == 'selectbackground':
                return s._canvas['background']
            elif item == 'selectforeground':
                return s._canvas.itemcget(s._canvas.text, 'fill')
            else:
                r = ttk.tclobjs_to_py({item: ttk.Frame.__getitem__(s, item)})
                return r[item]

        def __setup_styles(s):
            # 自定義TTK風格
            style = ttk.Style(s.master)

            def arrow_layout(dir): return (
                [('Button.focus', {'children': [
                  ('Button.%sarrow' % dir, None)]})]
            )
            style.layout('L.TButton', arrow_layout('left'))
            style.layout('R.TButton', arrow_layout('right'))

        def __place_widgets(s):
            # 標頭框架及其小部件
            Input_judgment_num = s.master.register(
                s.Input_judgment)  # 需要将函数包装一下，必要的
            hframe = ttk.Frame(s.G_Frame)
            gframe = ttk.Frame(s.G_Frame)
            bframe = ttk.Frame(s.G_Frame)
            hframe.pack(in_=s.G_Frame, side='top', pady=5, anchor='center')
            gframe.pack(in_=s.G_Frame, fill=tk.X, pady=5)
            bframe.pack(in_=s.G_Frame, side='bottom', pady=5)
            lbtn = ttk.Button(hframe, style='L.TButton', command=s._prev_month)
            lbtn.grid(in_=hframe, column=0, row=0, padx=12)
            rbtn = ttk.Button(hframe, style='R.TButton', command=s._next_month)
            rbtn.grid(in_=hframe, column=5, row=0, padx=12)
            s.CB_year = ttk.Combobox(hframe, width=5, values=[str(year) for year in range(datetime.now(
            ).year, datetime.now().year-11, -1)], validate='key', validatecommand=(Input_judgment_num, '%P'))
            s.CB_year.current(0)
            s.CB_year.grid(in_=hframe, column=1, row=0)
            s.CB_year.bind('<KeyPress>', lambda event: s._update(event, True))
            s.CB_year.bind("<<ComboboxSelected>>", s._update)
            tk.Label(hframe, text='年', justify='left').grid(
                in_=hframe, column=2, row=0, padx=(0, 5))
            s.CB_month = ttk.Combobox(hframe, width=3, values=[
                '%02d' % month for month in range(1, 13)], state='readonly')
            s.CB_month.current(datetime.now().month - 1)
            s.CB_month.grid(in_=hframe, column=3, row=0)
            s.CB_month.bind("<<ComboboxSelected>>", s._update)
            tk.Label(hframe, text='月', justify='left').grid(
                in_=hframe, column=4, row=0)
            # 日历部件
            s._calendar = ttk.Treeview(
                gframe, show='', selectmode='none', height=7)
            s._calendar.pack(expand=1, fill='both', side='bottom', padx=5)
            ttk.Button(bframe, text="確 定", width=6, command=lambda: s._exit(
                True)).grid(row=0, column=0, sticky='ns', padx=20)
            ttk.Button(bframe, text="取 消", width=6, command=s._exit).grid(
                row=0, column=1, sticky='ne', padx=20)
            tk.Frame(s.G_Frame, bg='#565656').place(
                x=0, y=0, relx=0, rely=0, relwidth=1, relheigh=2/200)
            tk.Frame(s.G_Frame, bg='#565656').place(
                x=0, y=0, relx=0, rely=198/200, relwidth=1, relheigh=2/200)
            tk.Frame(s.G_Frame, bg='#565656').place(
                x=0, y=0, relx=0, rely=0, relwidth=2/200, relheigh=1)
            tk.Frame(s.G_Frame, bg='#565656').place(
                x=0, y=0, relx=198/200, rely=0, relwidth=2/200, relheigh=1)

        def __config_calendar(s):
            # cols = s._cal.formatweekheader(3).split()
            cols = ['日', '一', '二', '三', '四', '五', '六']
            s._calendar['columns'] = cols
            s._calendar.tag_configure('header', background='grey90')
            s._calendar.insert('', 'end', values=cols, tag='header')
            # 調整其列寬
            font = tkFont.Font()
            maxwidth = max(font.measure(col) for col in cols)
            for col in cols:
                s._calendar.column(col, width=maxwidth, minwidth=maxwidth,
                                   anchor='center')

        def __setup_selection(s, sel_bg, sel_fg):
            def __canvas_forget(evt):
                canvas.place_forget()
                s._selection = None

            s._font = tkFont.Font()
            s._canvas = canvas = tk.Canvas(
                s._calendar, background=sel_bg, borderwidth=0, highlightthickness=0)
            canvas.text = canvas.create_text(0, 0, fill=sel_fg, anchor='w')
            canvas.bind('<Button-1>', __canvas_forget)
            s._calendar.bind('<Configure>', __canvas_forget)
            s._calendar.bind('<Button-1>', s._pressed)

        def _build_calendar(s):
            year, month = s._date.year, s._date.month
            header = s._cal.formatmonthname(year, month, 0)
            # 更新日曆顯示的日期
            cal = s._cal.monthdayscalendar(year, month)
            for indx, item in enumerate(s._items):
                week = cal[indx] if indx < len(cal) else []
                fmt_week = [('%02d' % day) if day else '' for day in week]
                s._calendar.item(item, values=fmt_week)

        def _show_select(s, text, bbox):
            x, y, width, height = bbox
            textw = s._font.measure(text)
            canvas = s._canvas
            canvas.configure(width=width, height=height)
            canvas.coords(canvas.text, (width - textw)/2, height / 2 - 1)
            canvas.itemconfigure(canvas.text, text=text)
            canvas.place(in_=s._calendar, x=x, y=y)

        def _pressed(s, evt=None, item=None, column=None, widget=None):
            # 在日歷的某個地方點擊
            if not item:
                x, y, widget = evt.x, evt.y, evt.widget
                item = widget.identify_row(y)
                column = widget.identify_column(x)
            if not column or not item in s._items:
                # 在工作日行中單擊或僅在列外單擊。
                return
            item_values = widget.item(item)['values']
            if not len(item_values):  # 這個月的行是空的。
                return
            text = item_values[int(column[1]) - 1]
            if not text:
                return
            bbox = widget.bbox(item, column)
            if not bbox:  # 日歷尚不可見
                s.master.after(20, lambda: s._pressed(
                    item=item, column=column, widget=widget))
                return
            text = '%02d' % text
            s._selection = (text, item, column)
            s._show_select(text, bbox)

        def _prev_month(s):
            # 更新日歷以顯示前一個月
            s._canvas.place_forget()
            s._selection = None
            s._date = s._date - timedelta(days=1)
            s._date = datetime(s._date.year, s._date.month, 1)
            s.CB_year.set(s._date.year)
            s.CB_month.set(s._date.month)
            s._update()

        def _next_month(s):
            # 更新日歷以顯示下一個月
            s._canvas.place_forget()
            s._selection = None

            year, month = s._date.year, s._date.month
            s._date = s._date + timedelta(
                days=calendar.monthrange(year, month)[1] + 1)
            s._date = datetime(s._date.year, s._date.month, 1)
            s.CB_year.set(s._date.year)
            s.CB_month.set(s._date.month)
            s._update()

        def _update(s, event=None, key=None):
            # 刷新界面
            if key and event.keysym != 'Return':
                return
            year = int(s.CB_year.get())
            month = int(s.CB_month.get())
            if year == 0 or year > 9999:
                return
            s._canvas.place_forget()
            s._date = datetime(year, month, 1)
            s._build_calendar()  # 重建日歷
            if year == datetime.now().year and month == datetime.now().month:
                day = datetime.now().day
                for _item, day_list in enumerate(s._cal.monthdayscalendar(year, month)):
                    if day in day_list:
                        item = 'I00' + str(_item + 2)
                        column = '#' + str(day_list.index(day)+1)
                        s.master.after(100, lambda: s._pressed(
                            item=item, column=column, widget=s._calendar))

        def _exit(s, confirm=False):
            if not confirm:
                s._selection = None
            s.master.destroy()

        def _main_judge(s):
            # 判斷窗口是否在最頂層
            try:
                if s.master.focus_displayof() == None or 'toplevel' not in str(s.master.focus_displayof()):
                    s._exit()
                else:
                    s.master.after(10, s._main_judge)
            except:
                s.master.after(10, s._main_judge)

        def selection(s):
            # 返回表示當前選定日期的日期時間
            if not s._selection:
                return None
            year, month = s._date.year, s._date.month
            return str(datetime(year, month, int(s._selection[0])))[:10]

        def Input_judgment(s, content):
            # 輸入判斷
            if content.isdigit() or content == "":
                return True
            else:
                return False

    class datepicker:
        def __init__(s, window, axes):  # 窗口對象 座標
            s.window = window
            s.frame = tk.Frame(s.window, padx=5)
            s.frame.grid(row=axes[0], column=axes[1])
            s.start_date = tk.StringVar()  # 開始日期
            s.end_date = tk.StringVar()  # 結束日期
            s.bt1 = tk.Button(s.frame, text='開始',
                              command=lambda: s.getdate('start'))  # 開始按鈕
            s.bt1.grid(row=1, column=0)
            s.ent1 = tk.Entry(s.frame, textvariable=s.start_date)  # 開始輸入框
            s.ent1.grid(row=1, column=1)
            s.bt2 = tk.Button(s.frame, text='結束',
                              command=lambda: s.getdate('end'))
            s.bt2.grid(row=1, column=2)
            s.ent2 = tk.Entry(s.frame, textvariable=s.end_date)
            s.ent2.grid(row=1, column=3)
            button = tk.Button(window, text="輸出查詢結果", command=close_window)
            button.grid(row=2, column=1)

        def getdate(s, type):  # 獲取選擇的日期
            for date in [Calendar().selection()]:
                if date:
                    if(type == 'start'):  # 如果是開始按紐，就賦值給開始日期
                        s.start_date.set(date)
                        global st_date
                        st_date = date
                        print(date)
                    elif(type == 'end'):
                        s.end_date.set(date)
                        global ed_date
                        ed_date = date
                        print(date)

    def close_window():
        window.destroy()

    # 執行
    if __name__ == '__main__':
        # window = tk.Tk()  # //
        window = tk.Toplevel(mwindow)  # //
        window.title("window")
        window.wm_attributes('-topmost', True)  # 窗口置頂
        tk.Label(window, text='日期段:').grid(row=0, column=0)
        obj = datepicker(window, (0, 1))  # 初始化類為對象
        startstamp1 = obj.start_date.get()  # 獲取開始時期
        endstamp1 = obj.end_date.get()

        # tk.Label(window,text='日期段二:').grid(row=1,column=0)
        # obj=datepicker(window,(1,1))
        # startstamp2=obj.start_date.get()
        # endstamp2=obj.end_date.get()
        tk.Button(window, text="print",
                  command=close_window)
        window.geometry("450x400")
        window.title("調閱收支")
        window.configure(bg='red')
        window.wait_window()
        # window.mainloop()

    def stat():
        # 設讀取資料型態[[收入／支出,日期,類別,金額]]
        # thisrev 為已經篩選出時間範圍內的收入資料list
        # thisexp 為已經篩選出時間範圍內的支出資料list
        global food_exp, clothing_exp, living_exp, trans_exp, learning_exp, entertainment_exp, medical_exp
        global salary, wage, allowance
        """food_exp = 0  # 食
        clothing_exp = 0  # 衣
        living_exp = 0  # 住
        trans_exp = 0  # 行
        learning_exp = 0  # 育
        entertainment_exp = 0  # 樂
        medical_exp = 0  # 醫療

        salary = 0  # 薪資
        wage = 0  # 打工
        allowance = 0  # 零用"""

        # 計算收入各類別總金額
        # global gvar.thisrev, gvar.thisexp
        for data in gvar.thisexp:
            if data[2] == '食':
                food_exp += int(data[3])
            elif data[2] == '衣':
                clothing_exp += int(data[3])
            elif data[2] == '住':
                living_exp += int(data[3])
            elif data[2] == '行':
                trans_exp += int(data[3])
            elif data[2] == '育':
                learning_exp += int(data[3])
            elif data[2] == '樂':
                entertainment_exp += int(data[3])
            elif data[2] == '醫療':
                medical_exp += int(data[3])

        # 計算收入各類別總金額
        # print(thisrev)
        for data in gvar.thisrev:
            if data[2] == '薪資':
                salary += int(data[3])
            elif data[2] == '打工':
                wage += int(data[3])
            elif data[2] == '零用':
                allowance += int(data[3])

        #  以下為支出圓餅圖的部分

        fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect='equal'))
        fig.patch.set_facecolor('black')

        labels = ['food', 'clothing', 'living', 'transportation',
                  'learning', 'entertainment', 'medical_care']
        exp = [food_exp, clothing_exp, living_exp, trans_exp,
               learning_exp, entertainment_exp, medical_exp]
        color = ['mistyrose', 'bisque', 'lavender', 'lightcyan',
                 'honeydew', 'lightgray', 'paleturquoise']

        wedges, texts, auto = ax.pie(exp, wedgeprops=dict(
            width=0.5), startangle=-40, colors=color, autopct='%.1f%%', pctdistance=0.85)

        bbox_props = dict(boxstyle='square,pad=0.3', fc='w', ec='k', lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle='-'),
                  bbox=bbox_props, zorder=0, va='center')

        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})

        ax.set_title("Donut for expense")

        plt.legend(wedges, labels, loc='best', bbox_to_anchor=(-0.1, 1.),
                   fontsize=8)

        # plt.show()
        plt.savefig('exp_donut.jpg')
        plt.clf()
        # 以下為收入圓餅圖部分

        fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect='equal'))
        fig.patch.set_facecolor('black')

        labels_rev = ['salary', 'wage', 'allowance']
        rev = [salary, wage, allowance]
        color = ['mistyrose', 'bisque', 'lavender']

        wedges, texts, auto = ax.pie(rev, wedgeprops=dict(
            width=0.5), startangle=-40, colors=color, autopct='%.1f%%', pctdistance=0.85)

        bbox_props = dict(boxstyle='square,pad=0.3', fc='w', ec='k', lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle='-'),
                  bbox=bbox_props, zorder=0, va='center')

        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})

        ax.set_title("Donut for revenue")

        plt.legend(wedges, labels_rev, loc='best', bbox_to_anchor=(-0.1, 1.),
                   fontsize=8)
        plt.savefig('rev_donut.jpg')

    """輸出結果為表格形式"""
    # exp = [["支出", "2020/10/20", "午餐", "168"], ["支出", "2020/10/21", "午餐", "100"]]
    # exp = ["2020-10-20, 支出, 午餐, 168", "2020-10-25, 支出, 晚餐,98"]
    # rev = [["收入", "2020/11/02", "家教", "800"]]

    result = tk.Toplevel()
    result.title("result")
    tree = ttk.Treeview(result)  # 表格
    tree["columns"] = ("收支", "時間", "類別", "金額")
    tree.column("收支", width=100)
    tree.column("時間", width=200)  # 表示列,不顯示
    tree.column("類別", width=100)
    tree.column("金額", width=100)

    tree.heading("收支", text="收支")
    tree.heading("時間", text="時間")  # 顯示錶頭
    tree.heading("類別", text="類別")
    tree.heading("金額", text="金額")

    # print("#" + st_date)
    # print("#" + ed_date)

    st_dt = r_datetime.datetime.strptime(st_date, "%Y-%m-%d")
    lf_date = (st_dt + r_datetime.timedelta(days=-1)).strftime("%Y/%m/%d")
    # rt_date = (ed_dt + r_datetime.timedelta(days=1)).strftime("%Y/%m/%d")
    rt_date = ed_date.replace('-', '/')
    """收入的範圍"""
    lf_line = ["收入", lf_date, "", ""]
    rt_line = ["收入", rt_date, "", ""]

    lf_pos = func.bisearch(gvar.rev, lf_line)
    rt_pos = func.bisearch(gvar.rev, rt_line)

    gvar.thisrev = gvar.rev[lf_pos:rt_pos]
    # print(thisrev)
    # for i in range(lf_pos, rt_pos):
    # tree.insert("", i, values=(gvar.rev[i][0], gvar.rev[i]
    #    [1], gvar.rev[i][2], gvar.rev[i][3]))  # 插入資料
    for i in range(len(gvar.thisrev)):
        tree.insert("", i, values=(
            gvar.thisrev[i][0], gvar.thisrev[i][1], gvar.thisrev[i][2], gvar.thisrev[i][3]))
    lf_line = ["支出", lf_date, "", ""]
    rt_line = ["支出", rt_date, "", ""]
    lf_pos = func.bisearch(gvar.exp, lf_line)
    rt_pos = func.bisearch(gvar.exp, rt_line)

    gvar.thisexp = gvar.exp[lf_pos:rt_pos]
    for i in range(lf_pos, rt_pos):
        tree.insert("", i, values=(gvar.exp[i][0], gvar.exp[i]
                                   [1], gvar.exp[i][2], gvar.exp[i][3]))  # 插入資料
    tree.pack()
    # print_graph()
    stat()
    show_catog = tk.Button(result, text='類別統計', command=showcatog)
    show_catog.pack()
    show_donut = tk.Button(result, text="圓餅圖", command=showpic)
    show_donut.pack()
    # show_edonut = tk.Button(root, text="show picture", command=showpic(rev_donut.jpg))
    result.configure(bg='red')
    result.wait_window()
    # result.mainloop()
    # root.mainloop()


"""Button 指令整理"""
# 主頁


def homewin():
    add_new_data.do()
    update_data_file.do()

# 統計


def statwin():
    timecalendar()

# 心情


def askemoji():
    emoji.do()


read_old_data.do()
print(gvar.rev)

mwindow = tk.Tk()
mwindow.iconbitmap('homeicon.ico')
mwindow.title("Test")

menubar = tk.Menu(mwindow)
# menubar.add_command(label="主頁", command=homewin)
# menubar.add_command(label="明細", command = )
menubar.add_command(label="統計", command=statwin)
menubar.add_command(label="心情", command=askemoji)
menubar.add_command(label="退出", command=mwindow.quit)
mwindow.config(menu=menubar)
mwindow.title('記帳小幫手')
mwindow.geometry('800x600')
mwindow.configure(background='pink')

header_label = tk.Label(mwindow, text='記帳小幫手')
header_label.pack()
img_open = Image.open('homeicon.ico')
img_jpg = ImageTk.PhotoImage(img_open)
home_icon = tk.Label(mwindow, image=img_jpg)
home_icon.pack()

#  支出/收入、日期、類別、金額

#  以下為支出/收入下拉式選單的部分
nopt = tk.StringVar()
options = ('收入', '支出')
option = ttk.Combobox(mwindow, width=30, textvariable=nopt, values=options)
option.pack(side=tk.TOP)

#  以下為使用者輸入日期的部分
ndate = tk.StringVar()
date_frame = tk.Frame(mwindow)
date_frame.pack(side=tk.TOP)
date_label = tk.Label(date_frame, text='日期：(xxxx/xx/xx)')
date_label.pack(side=tk.LEFT)
date_entry = tk.Entry(date_frame, textvariable=ndate)
date_entry.pack(side=tk.LEFT)

#  以下為類別下拉式選單的部分
ncat = tk.StringVar()
categories = ('食', '衣', '住', '行', '育', '樂', '醫療', '薪資', '打工', '零用')
category = ttk.Combobox(
    mwindow, width=30, textvariable=ncat, values=categories)
category.pack(side=tk.TOP)

#  以下為金額的部分
nmoney = tk.StringVar()
money_frame = tk.Frame(mwindow)
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
        pos = func.bisearch(gvar.rev, line)
        gvar.rev.insert(pos, line)
    elif(cur_opt == "支出"):
        pos = func.bisearch(gvar.exp, line)
        gvar.exp.insert(pos, line)
    else:
        messagebox.showinfo("輸入錯誤", "數值錯誤")
    update_data_file.do()


press = tk.Button(mwindow, text="新增", command=getdata)
press.pack()

mwindow.mainloop()
