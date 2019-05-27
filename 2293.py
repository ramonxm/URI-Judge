n, m = input().split()
n, m = int(n), int(m)

matriz = []

for i in range(n):
    linha = input()
    lista_str = linha.split()
    #lista = [int(x) for x in lista]

    lista_int = []

    for x in lista_str:
        lista_int.append(int(x))

    matriz.append(lista_int)

#nao_sei = True
melhor = None

for i in range(n):
    soma = 0
    for j in range(m):
        soma += matriz[i][j]

    if melhor == None:
        melhor = soma
    else:
        melhor = max(melhor, soma)

for j in range(m):
    soma = 0

    for i in range(n):
        soma += matriz[i][j]

    melhor = max(melhor, soma)

print(melhor)
