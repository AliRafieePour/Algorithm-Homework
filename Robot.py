try:
    import Queue as Q
except:
    import queue as Q
class Node:
    def __init__(self, a, b, c, d):
        self.x = a
        self.y = b
        self.dir = c
        self.time = d
def st(a, b, c, d, e):
    #global di 
    #global dj
    global somethingcute
    global vv
    myqueue = Q.Queue()
    if valid(a, b):
        myqueue.put(Node(a, b, c, 0))
        vv[a][b][c] = True
    while(myqueue.empty()== False):
        mynode = myqueue.get()
        if mynode.x == d and mynode.y == e:
            return mynode.time
        if (vv[mynode.x][mynode.y][(mynode.dir + 1) % 4]== False):
            vv[mynode.x][mynode.y][(mynode.dir + 1) % 4] = True
            myqueue.put(Node(mynode.x, mynode.y, (mynode.dir + 1) % 4, mynode.time + 1))
        if (vv[mynode.x][mynode.y][(mynode.dir + 3) % 4] == False):
            vv[mynode.x][mynode.y][(mynode.dir + 3) % 4] = True
            myqueue.put(Node(mynode.x, mynode.y, (mynode.dir + 3) % 4, mynode.time + 1))
        for i in range (1, 4, 1):
            if valid(mynode.x + somethingcute[mynode.dir][0] * i, mynode.y + somethingcute[mynode.dir][1] * i):
                try:
                    if vv[mynode.x + somethingcute[mynode.dir][0] * i][mynode.y + somethingcute[mynode.dir][1] * i][mynode.dir]:
                        continue
                    vv[mynode.x + somethingcute[mynode.dir][0] * i][mynode.y + somethingcute[mynode.dir][1] * i][mynode.dir] = True
                    myqueue.put(Node(mynode.x + somethingcute[mynode.dir][0] * i, mynode.y + somethingcute[mynode.dir][1] * i, mynode.dir, mynode.time + 1))
                except Exception as e:
                    print('{}   {}   {}   {}'.format(mynode.x + somethingcute[mynode.dir][0] * i, mynode.y + somethingcute[mynode.dir][1] * i, mynode.dir, e))
                    exit()

            else:
                break
    return -1
def valid(x, y):
    global M
    global N
    global obs
    if x <=0 or y <= 0 or x >= M or y >= N:
        return False
    if obs[x - 1][y - 1]:
        return False
    if obs[x - 1][y]:
        return False
    if obs[x][y - 1]:
        return False
    if obs[x][y]:
        return False
    return True
#di = [-1,0,1,0]
#dj = [0,1,0,-1]
somethingcute = [(-1, 0), (0, 1), (1, 0), (0, -1)]
firstline = input().split(' ')
firstline = [int(x) for x in firstline]
M = firstline[0]
N = firstline[1]
vv =[[[False for x in range(4)] for x in range(N)] for x in range(M)]
obs = []
for i in range(M):
    line = input().split(' ')
    line = [int(x) for x in line]
    obs.append(line)
lastline = input().split(' ')
startx = int(lastline[0])
starty = int(lastline[1])
endx = int(lastline[2])
endy = int(lastline[3])
pos = lastline[4]
if(pos == 'north'): dir = 0
elif(pos == 'east'): dir = 1
elif(pos == 'south'): dir = 2
else: dir = 3
print(st(startx, starty, dir, endx, endy))