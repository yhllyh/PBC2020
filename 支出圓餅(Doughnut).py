import matplotlib.pyplot as plt
import numpy as np
import timecalendar as tc
# 設讀取資料型態[[收入／支出,日期,類別,金額]]
# thisrev 為已經篩選出時間範圍內的收入資料list
# thisexp 為已經篩選出時間範圍內的支出資料list

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

# 計算收入各類別總金額

for data in thisrev:
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

# 計算支出各類別總金額

for data in thisexp:
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

plt.show()
