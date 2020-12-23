from tkinter import ttk  # 匯入內部包
import calendar
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
datetime = calendar.datetime.datetime
timedelta = calendar.datetime.timedelta

"""用日曆選擇想要查的時間段"""


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
        s._items = [s._calendar.insert('', 'end', values='') for _ in range(6)]
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
            [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
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
        # 更新日歷顯示的日期
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
        s.bt2 = tk.Button(s.frame, text='結束', command=lambda: s.getdate('end'))
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
                    print(date)
                elif(type == 'end'):
                    s.end_date.set(date)
                    print(date)


def close_window():
    window.destroy()


# 執行
if __name__ == '__main__':
    window = tk.Tk()
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
    window.mainloop()


"""讀取以前資料
rev = []
exp = []
with open(file='data.txt', mode='r', encoding='utf-8') as f:
    change = False
    for line in f:
        line = line.strip()
        if line == "ExpEnd" or line == "RevEnd":
            change = not True
            continue
        line = line.split()
        if change:
            rev.append(line)
        else:
            exp.append(line)
"""


"""輸出結果為表格形式"""

exp = ["2020-10-20, 支出, 午餐, 168", "2020-10-25, 支出, 晚餐,98"]
rev = ["2020-11-02, 收入, 家教, 800"]


result = tk.Tk()
tree = ttk.Treeview(result)  # 表格
tree["columns"] = ("時間", "類別", "收支", "金額")
tree.column("時間", width=200)  # 表示列,不顯示
tree.column("收支", width=100)
tree.column("類別", width=100)
tree.column("金額", width=100)

tree.heading("時間", text="時間")  # 顯示錶頭
tree.heading("收支", text="收支")
tree.heading("類別", text="類別")
tree.heading("金額", text="金額")

for i in range(len(rev)):
    word = rev[i].split(",")
    tree.insert("", i, values=(word[0], word[1], word[2], word[3]))  # 插入資料

for i in range(len(exp)):
    word = exp[i].split(",")
    tree.insert("", i, values=(word[0], word[1], word[2], word[3]))  # 插入資料


tree.pack()
result.configure(bg='red')
result.mainloop()