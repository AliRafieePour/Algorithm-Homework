distance = int(input())
colm = (distance//100) + 1
rows = (distance//100)
matris = [[0 for x in range (colm)] for y in range(10)]
for i in range(rows):
    for j in range(colm):
        if ((distance!= (100*j)) and i==0):
            matris[i][j] = 10e9
        if (distance!=(100*j) and j==0):
            matris[i][j] = 10e9
for o in range(rows,10):
    for oo in range(colm):
        matris[o][oo] = 10e9
matris[0][0] = 0
wind = [[0 for kk in range(colm)] for zz in range(10)]
for ii in range(9,-1,-1):
    entry = input().split(sep=' ')
    for jj in range(1,colm):
        wind[ii][jj] = int(entry[jj-1])
for m in range(1,colm):
    for n in range(1,rows):
        if n==(rows-1):
            matris[n][m] = min(matris[n][m - 1] + 30 - wind[n][m],
                               matris[n - 1][m - 1] + 60 - wind[n][m])
        else:
            matris[n][m] = min(matris[n][m - 1] + 30 - wind[n][m],
                               matris[n + 1][m - 1] + 20 - wind[n][m],
                               matris[n - 1][m - 1] + 60 - wind[n][m])
print(min(matris[0][colm-2]+30-wind[0][colm-1],
          matris[1][colm-2]+20-wind[0][colm-1]))