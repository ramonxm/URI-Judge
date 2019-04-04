t = 1
while True:
    q = 0
    p = 0
    V = int(input())
    if V == 0:
        break
    print('Teste {}'.format(t))
    t += 1
    while V > 0:
        V -= 1
        A, B = [int(x) for x in input().split()]
        q += A
        p += B
    if q > p:
          print('Aldo')
          print()
    elif p >= q:
          print('Beto')
          print()
