t = 1
while True :
    n = int(input())
    if  n == 0:
        break
    Name1 = input()
    Name2 = input()
    print('Teste {}'.format(t))
    
    t += 1
    
    while n > 0:
        A,B = map(int,input().split())
        
        if (A + B) % 2 == 0:
            print(Name1)
        else: 
            print(Name2)
            
        n -= 1
    print()
