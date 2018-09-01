def func(l):
    global ma
    global _seen
    global count
    if _seen[l] == True:
        return
    _seen[l] = True
    count += 1
    func(ma[l])

_seen = {}
num = int(input())
ma = {}
for i in range(num):
    st = input().split(' ')
    ma[st[0]] = st[1]
    _seen[st[0]] = False
li = {}
for k in ma.keys():
    for i in _seen:
        _seen[i] = False
    count = 0
    func(k)
    li[k] = count
max = -999
maxi = -99
for g in li.keys():
    if li[g]> max:
        max = li[g]
        maxi = g
print(maxi)