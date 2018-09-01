try:
    import Queue as Q
except:
    import queue as Q
class node:
    def __init__(self, r, c, w):
        self.row = r
        self.col = c
        self.cost = w
    def __gt__(self, x):
        return self.cost > x.cost
    def prin(self):
        print ("column={} row={} cost={}".format(self.col,self.row,self.cost))
NumofRow = int(input())
NumofCol = int(input())
BestMatris = [[-1 for x in range (NumofCol)] for y in range (NumofRow)]
SeenMatris = [[False for x in range (NumofCol)] for y in range (NumofRow)]
CostMatris = []
for i in range(NumofRow):
    _row = input().split(' ')
    _row = [int(x) for x in _row]
    CostMatris.append(_row)
Qu = Q.PriorityQueue()
Node = node(0, 0, CostMatris[0][0])
Qu.put(Node)
BestMatris[0][0] = CostMatris[0][0]
Dir =[(0, 1), (0, -1), (1, 0), (-1, 0)]
while(True):
    G = Qu.get()
    if SeenMatris[G.row][G.col]:
        continue
    SeenMatris[G.row][G.col] = True
    if (G.row == (NumofRow-1) and G.col == (NumofCol-1)):
        print(G.cost)
        break
    for k in range(4):
        RR = G.row + Dir[k][0]
        CC = G.col + Dir[k][1]
        if (RR>=0 and RR<NumofRow and CC>=0 and CC<NumofCol and (BestMatris[RR][CC] == -1 or BestMatris[RR][CC]>BestMatris[G.row][G.col] + CostMatris[RR][CC])):
            BestMatris[RR][CC] = BestMatris[G.row][G.col] + CostMatris[RR][CC]
            Nodee = node(RR, CC, BestMatris[RR][CC])
            Qu.put(Nodee)