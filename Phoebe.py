import matplotlib.pyplot as plt  # 畫畫的那個程式
import datetime  # 日期的那個程式
want = int(input())  # 先這樣放，就是使用者要的天數
if want < 1:  # 別人輸入亂碼的話怎麼辦~~~
    want = 1  # 如果數字小於0就直接當作他=1
把檔案讀出來
category = []  # 有消費到的類別。之後要轉成tuple
money_category = []  # 類別對應到的金額，之後要轉成dictionary[money,category]

for i in range(看看這裡總共有多少筆帳):
    這邊放要怎麼讀當次資料
    a = 先看資料怎麼取  # 帳本上的年
    b = 先看資料怎麼取  # 帳本上的月
    c = 先看資料怎麼取  # 帳本上的日
    date = datetime.datetime(a, b, c)  # 帳本上的那天日期
    today = str(datetime.date.today())
    today = today.split('-')
    today_year = int(today[0])
    today_month = int(today[1])
    today_day = int(today[2])
    diff = datetime.datetime(today_year, today_month, today_day) - datetime.datetime(a, b, c)
    diff = str(diff)
    diff = diff.split(',')
    diff = int(diff[0][:-5])  # 今天跟那天差幾天
    if diff <= want:  # 在指定範圍內
        if category.count(那個類別名稱) == 1:  # 之前已經有同類別的帳了
            money_category[category.index(那個類別名稱)][1] += int(這筆錢)
        elif category.count(那個類別名稱) == 0 :  # 之前還沒有同類別的帳了
            category.append(那個類別名稱)
            money_category.append([那個類別名稱, int(這次的金額)])
# 現在應該會有category的list、category配對對應金額的list
# 現在把category的list轉成tuple、把有金額的那個list轉成dictionary
total_amount = 0  # 這段期間總消費
labels = tuple(category)
category_money = dict()
for i in range(len(category)):
    total_amount += money_category[i][1]
for i in range(len(category)):
    percent = money_category[i][1]/total_amount
    category_money[money_category[i][0]] = str(percent)
# 現在應該有tuple跟對應的dictionary了
sizes = []
for i in range(len(labels)):
    sizes.append(category_money.get(labels[i]))
# 現在labels存資料、sizes存比例
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

'''
category = []  # 有消費到的類別。之後要轉成tuple
money_category = []  # 類別對應到的金額，之後要轉成dictionary
# 把所有有出現的類別放進category
'''


'''
用之前學的日期回推幾天之前的資料
total = 所有時間內的消費加一起
生出一個負責確認有沒有這個類別的list
生出一個負責計算所有類別的價錢分別有多少錢
所有類別分門別類把他們加一起存到上面那個第二個list
最後根據list裡面的data生出圓餅圖
'''
# 注意如果當天沒消費
# 數字小於0
'''
網路上的example
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
'''