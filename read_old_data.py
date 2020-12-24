import gvar
def do():
    with open(file='data.txt', mode='r', encoding='utf-8') as f:
        change = False
        for line in f:
            line = line.strip()
            if line == "ExpEnd" or line == "RevEnd":
                change = not change
                continue
            line = line.split()
            if change:
                gvar.rev.append(line)
            else:
                gvar.exp.append(line)
