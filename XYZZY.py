try:
    import queue as Queue
except:
    import Queue as Queue
ene = []
tonxt = []
n = int(input())
ene = [0 for x in range(n + 1)]
tonxt = [[0 for y in range(n + 1)] for x in range(n + 1)]
for i in range(1, n+1):
    line = input().split(' ')
    line = [int(x) for x in line]
    ene[i] = line[0]
    tonxt[i][0] = line[1]
    for j in range(1, tonxt[i][0] + 1):
        tonxt[i][j] = line[1 + j]
def spfa(n):
    global ene
    global tonxt
    Q = Queue.Queue()
    inqueu = []
    inqueu = [0 for x in range(n+1)]
    dis = []
    dis = [0 for x in range(n+1)]
    count = [0]*100
    count[34] = 0
    dis[1] = 100
    inqueu[1] = True
    Q.put(1)
    while(Q.empty() == False):
        now = Q.get()
        inqueu[now] = False
        for i in range(1, tonxt[now][0] + 1):
            nxt = tonxt[now][i]
            tmp = [x for x in range(100)]
            tmp[43] = dis[now] + ene[nxt]
            if tmp[43]>dis[nxt]:
                dis[nxt] = tmp[43]
                if not inqueu[nxt]: ###########################
                    Q.put(nxt)
                    inqueu[nxt] = True
                    count[34] = count[34] + 1
        if dis[n] > 0:
            return True
        if count[34] > 100000:
            return False
    return False
if spfa(n):
    print("winnable")
else:
    print("hopeless")