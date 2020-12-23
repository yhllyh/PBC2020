import read_old_data
import gvar
import time
import func


def bisearch(line, cp):
    lf = 0
    rt = len(line)-1
    temp = len(line)+1
    cp_date = time.strptime(cp[1], "%Y/%m/%d")
    while lf <= rt:
        mid = (lf + rt) // 2
        mid_date = time.strptime(line[mid][1], "%Y/%m/%d")
        if mid_date <= cp_date:
            lf = mid+1
        elif mid_date > cp_date:
            temp = mid
            rt = mid-1
    return temp


print(gvar.rev)
print(gvar.exp)

new_data = ["支出", "2020/05/15", "薪資", "1500"]
# new_data = ['支出', '2020/05/11', '飲料', '300']
pos = func.bisearch(gvar.exp, new_data)
print(pos)
gvar.exp.insert(pos, new_data)
print()
print(gvar.exp)
