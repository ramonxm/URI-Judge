a,b,c,d = map(int,input().split())
r,s,t,u = map(int,input().split())

intersecao_x = not(c < r or a > t) 
intersecao_y = not(d < s or b > u)

if intersecao_x and intersecao_y:
    print(1)
else:
    print(0)
