num = int(input())
beve = []
for i in range(num):
    beve.append(input())
tar = []
num2 = int(input())
for r in range(num2):
    stri = input().split(' ')
    tar.append(stri)
print("Dilbert should drink beverages in this order:", end=' ')
while len(tar)!=0:
    dele = []
    beve2 = beve.copy()
    for k in range(len(tar)):
        if tar[k][1] not in dele:
            beve2.remove(tar[k][1])
            dele.append(tar[k][1])
    z = 0
    b = len(tar)
    while len(tar) != 0:
        z += 1
        if z != b:
            for q in range(len(tar)):
                if tar[q][0] == beve2[0]:
                    del(tar[q])
                    break
        else:
            break
    if len(beve2) != 0:
        print(beve2[0], end=' ')
        beve.remove(beve2[0])
    else:
        print(beve[0], end='')
        break

print(".", end=' ')