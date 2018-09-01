start = 0
end = 0
j = 0
max2 = 0
def y(a, b):
    global start
    global end
    global max2
    max = 0
    c=[]
    for i in range(b):
        if a[i]>=(max+a[i]):
            max = a[i]
            c.append(max)
            start = i
        else:
            end = a[i]
            c.append(max+a[i])
            max = max+a[i]
        max2 = c[0]
    for i in range(b):
        if c[i]>=max2:
            max2 = c[i]
            end = i

a1 = int(input())
matris = [[0 for x in range(a1)] for y in range(a1)]
tedad = a1**2
ooo = input().split(sep=' ')
for v in range(a1):
    for x in range(a1):
        matris[v][x] = int(ooo.pop())
matris2 = [[0 for x in range(a1)] for y in range(a1)]
arr = []
max3 = 0
for t in range(a1):
    for i in range(t,a1,1):
        arr.clear()
        for j in range(a1):
            sum = 0
            for mm in range(t,i+1,+1):
                sum = sum + matris[j][mm]
            arr.append(sum)
        y(arr,arr.__len__())
        if max2>=max3:
            max3 = max2
print(max3)







