a = 0
while True:
    v = int(input())
        
    if v == 0:
        break
    a += 1 
    
    s = v//50
    t = (v%50)//10
    q = (v%50%10)//5
    r = (v%50%10%5)
    print('Teste {}'.format(a))
    print('{} {} {} {}'.format(s,t,q,r))
    print('')
