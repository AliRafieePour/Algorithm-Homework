def split(mylist=[]):
    global ts
    global ll
    global b
    len2 = len(mylist)
    devide = len2 // 2
    if len2 == 1:
        return mylist
    if ts == b:
        return mylist
    ts = ts+2
    p = mylist[:devide]
    q = mylist[devide:]
    pp = q+p
    if ts != b:
        teke1 = split(q)
        teke2 = split(p)
        ll = teke1 + teke2
        return ll
    else:
        return pp

ts = 1
ll = []
#a = int(input())
#b = int(input())
c = input()
xx = c.split(' ');
a = int(xx[0])
b = int(xx[1])
if b % 2 == 0:
    print(-1)
else:
    My_List = [x for x in range(1, a + 1, 1)]
    if b == 1:
        print(*My_List)
    else:
        new88list = split(My_List)
        print(*new88list)