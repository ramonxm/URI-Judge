divisoes = int(input())
x = 0
pedacos = list(map(int,input().split()))

for i in pedacos:
	x += i

y = x-divisoes
print(y)
