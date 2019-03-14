vezes = int(input())
total = 0

while vezes > 0:
     T,V = input().split()
     T,V = int(T), int(V)
     S = V*T
     vezes = vezes - 1
     total = total + S
     
print(total)
