import gvar
def do():
    try:
        f = open(file="data.txt", mode='w', encoding='utf-8')
        for item in gvar.exp:
            line = " ".join(item)
            f.write(line + "\n")
        f.write("ExpEnd\n")
        for item in gvar.rev:
            line = " ".join(item)
            f.write(line + "\n")
        f.write("RevEnd\n")
    finally:
        f.close()
