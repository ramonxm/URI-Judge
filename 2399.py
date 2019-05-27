vezes = int(input())

lista_zeros = [0 for i in range(vezes)]

for i in range(vezes):
	bomba = int(input())
	if bomba == 1 and (i) > 0:
		lista_zeros[i-1] += 1
	if bomba == 1:
		lista_zeros[i] += 1
	if bomba == 1 and (i+1) < vezes:
		lista_zeros[i+1] += 1

for i in lista_zeros:
	print (i)
