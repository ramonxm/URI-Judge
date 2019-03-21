vezes, saldo = map(int,input().split())
menor = saldo

while vezes > 0:
	x = int(input())
	saldo = saldo + x
	vezes = vezes - 1
	
	if saldo < menor:
		menor = saldo
		
print(menor)
