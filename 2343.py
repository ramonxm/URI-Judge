num_raios = int(input())
marcação = [[0 for j in range(501)] for i in range(501)]
saida = 0
for i in range(num_raios):
    x,y = map(int,input().split())
    if marcação[x][y] == 1:
        saida = 1
        break

    marcação[x][y] = 1

print(saida)
