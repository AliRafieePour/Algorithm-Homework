def dfs(x, y):
    global count
    global m
    global n
    global land
    global matris
    if (y < 0):
        y = m-1
    if (y >= m):
        y = 0
    if (x < 0 or x >= n):
        return
    if matris[x][y] == land:
        count += 1
        matris[x][y] = water
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
    else:
        return
count = 0
num = input().split(' ')
n = int(num[0])
m = int(num[1])
matris = []
for i in range(int(num[0])):
    matris.append([])
    stri = input()
    for j in range(int(num[1])):
        matris[i].append(stri[j])

cc = []
koja = input().split(' ')
koja[0] = int(koja[0])
koja[1] = int(koja[1])
land = matris[koja[0]][koja[1]]
water = "asas"
for k in range(n):
    for l in range(m):
        if matris[k][l] != land:
            water = matris[k][l]
            break
dfs(koja[0],koja[1])
cc.append(0)
for u in range(n):
    for t in range(m):
        if matris[u][t] != water:
            count = 0
            dfs(u,t)
            cc.append(count)
print (max(cc))