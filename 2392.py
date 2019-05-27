num_pedras, num_sapos = map(int, input().split())       
pedras = [0 for i in range(num_pedras)]

for i in range (num_sapos):
    pos_ini, salto = map(int, input().split())          
    pos_ini -= 1
    pedras[pos_ini] = 1

    esquerda = pos_ini - salto
    while esquerda >= 0:
        pedras[esquerda] = 1
        esquerda -= salto


    direita = pos_ini + salto
    while direita < num_pedras:
        pedras[direita] = 1
        direita += salto

for i in pedras:
    print(i)
