a1 = int(input())
if a1>=2000:
    a1 = a1 + 200
a2 = int(input())
gheymat = []
favour = []
gheymat.append(0)
favour.append(0)
for i in range(a2):
    v1 = input().split(sep=' ')
    gheymat.append(int(v1[0]))
    favour.append((int(v1[1])))
soton = int(a1/100)+1
matris = [[0 for y in range(a2+1)] for x in range(soton)]

for j in range(a2+1):
    matris[soton-1][j] = 0
for jj in range(soton):
    matris[jj][0] = 0
for m in range(1,soton,1):
    for n in range(1,a2+1,1):
        if ((m*100) - gheymat[n])<0:
            matris[m][n] = 0
        else:
            mmm = max(matris[m][n-1],matris[m-int(gheymat[n]/100)][n-1]+favour[n])
            matris[m][n] = mmm
print(matris[soton-1][a2])