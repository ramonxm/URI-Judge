x,y,r,s,a,b = map(int,input().split())

cabe = False 

altura = x + r
largura = min(y,s)

if (a <= altura  and b <= largura) or (a<= largura and b <= altura):
	cabe = True	

altura = x + s
largura = min(y,r)

if (a <= altura  and b <= largura) or (a<= largura and b <= altura):
	cabe = True	
	
altura = y + r
largura = min(x,s)

if (a <= altura  and b <= largura) or (a<= largura and b <= altura):
	cabe = True	
	
altura = y + s
largura = min(x,r)

if (a <= altura  and b <= largura) or (a<= largura and b <= altura):
	cabe = True	
	
altura = x
largura = y

if (a <= altura  and b <= largura) or (a<= largura and b <= altura):
	cabe = True	
	
altura = r
largura = s

if (a <= altura  and b <= largura) or (a<= largura and b <= altura):
	cabe = True	

if cabe:
	print('S')
else:
	print('N')
