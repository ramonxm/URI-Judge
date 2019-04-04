a = int(input())
n = int(input())
s = 0
q = 0
c = 0
while c < n:
    f = int(input())
    c += 1
    s = a*f
    if s >= 40000000:
        q += 1
    else:
        continue
print(q)
