v,t = map(int,input().split())
for x in input().split():
    x = int(x) 
    v += x
    if v < 0:
        v = 0
    if v > 100:
        v = 100
print(v)
