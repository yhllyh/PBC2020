import matplotlib.pyplot as plt

rev = []
exp = []

"""讀取以前資料"""
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

"""處理新的資料"""
print("Hello")
print("To record expense please press 0")
print("To record revenue please press 1")
while True:
    add = input()

"""整理+儲存資料"""
try:
    f = open(file="data.txt", mode='w', encoding='utf-8')
    for item in exp:
        line = " ".join(item)
        f.write(line)
    f.write("ExpEnd")
    for item in rev:
        line = " ".join(item)
        f.write(line)
    f.write("RevEnd")
finally:
    f.close()

"""TrashBin"""
# print(rev)
# print(exp)
"""
for item in exp:
        line = " ".join(item)
        f.write(line)
    f.write("ExpEnd")
    for item in rev:
        line = " ".join(item)
        f.write(line)
    f.write("RevEnd")
"""
