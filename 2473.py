n = list(map(int,input().split())) 
x = list(map(int,input().split()))
z = 0

for i in x:
    if i in n:
        z += 1
        
if z == 6:
    print('sena')
elif z == 5:
    print('quina')
elif z == 4:
    print('quadra')
elif z == 3:
    print('terno')
elif z < 3:
    print('azar')
