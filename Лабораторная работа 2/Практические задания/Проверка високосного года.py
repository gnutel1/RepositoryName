year = 2012
kk = range(0,2013,4)
ll = range(1,2012,100)
jj = range(1,2013,400)
if year in kk and (year not in ll and year not in jj):
    print(year, "является високосным годом.")
else:
    print(year, "не является високосным годом.")
