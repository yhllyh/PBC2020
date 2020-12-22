import matplotlib.pyplot as plt


rev = []
exp = []

with open(file='/Users/eileenyu/Desktop/data.txt', mode='r', encoding='utf-8') as f:
    while True:
        line = f.readline()

        print(line)

        if line == 'Y':
            break
        else:
            line = line.split(' ')
            if line[0] == '收入':
                rev.append(line)
            else:
                exp.append(line)

print(rev)
print(exp)
