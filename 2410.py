n = int(input())
a_p = [0 for i in range(10**6 +1)]
presentes = 0
for i in range(n):
    registro = int(input())
    if a_p[registro] == 0:
        a_p[registro] = 1
        presentes += 1
        
print(presentes)
