str = []
from sys import stdin
for str2 in stdin:
    str.append(str2)



inp = str.__len__()
for i in range(inp):
    str[i] = int(str[i])
j = []
for v in range(inp):
    j.append(0)
j[inp-1] = 1
hh = []
for k in range(inp-2,-1,-1): #mmmmmm77777mmmmmm000051150000mmmmmmmm77777mmmmmmmm
    max = 1
    for l in range(k,inp,1):
        tt = False
        if str[l]>str[k]:
            if (j[l]+1)>max:
                j[k] = j[l] + 1
                max = j[k]

            tt = True
    if tt!=True:
        j[k] = 1

mmm = 1
for b in range(len(j)):
    if mmm<j[b]:
        mmm = j[b]

gg = []
for p in range(mmm,0,-1):
    gg.append(j.count(p))
print(mmm)
print("-")
m1=0
for pp in range(mmm,0,-1):
    for hh in range(j.__len__()):
        if j[hh]==pp:
            m1 = hh
    print(str[m1])