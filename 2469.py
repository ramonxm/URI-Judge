n = int(input())

notas = [int(i) for i in input().split()]

m = [0 for x in range(101)]

for i in notas:
    m[i]+=1
    
pos=0
maior=0

for i in range(101):
    if maior <= m[i]:
        maior = m[i]
        pos = i
        
print(pos)
