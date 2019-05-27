indc = 1

while True:
    participantes = int(input())
    if participantes == 0:
            break    
    if participantes > 0:
        entradas = list(map(int,input().split()))
        for i in range(participantes):
            if entradas[i] == i+1:
                print("Teste",indc)
                indc += 1
                print(i+1)
                print()
