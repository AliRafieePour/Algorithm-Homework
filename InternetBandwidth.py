try:
    import queue as Q
except:
    import Queue as Q
def tabe(a, b, c, d, e):
    u = b[d]
    c = min(c, a[u][d])
    if u != e:
        c = tabe(a, b, c, u, e)
    a[u][d] -= c
    a[d][u] += c
    return c

n = int(input())
mymatrix =[[0 for x in range(n)] for x in range(n)]
firstline = input().split(' ')
start = int(firstline[0]) -1
end = int(firstline[1]) -1
num = int(firstline[2])
for i in range(int(num)):
    line = input().split(' ')
    line = [int(x) for x in line]
    try:
        mymatrix[line[0]-1][line[1]-1] += line[2]
        mymatrix[line[1]-1][line[0]-1] += line[2]
    except:
        for i in range(1000):
            print(i)
maxim = 0
while (True):
    lili = []
    for i in range(n):
        lili.append(-1)
    myqueue = Q.Queue()
    myqueue.put(start)
    lili[start] = start
    while (myqueue.empty()==False):
        u = myqueue.get()
        for g in range (0, n):
            if(mymatrix[u][g] > 0 and lili[g] == -1):
                lili[g] = u
                myqueue.put(g)
    if (lili[end] == -1):
        break
    maxim += tabe(mymatrix, lili, 1000, end, start)
print('The bandwidth is {}.'.format(maxim))
