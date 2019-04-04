z = -1
for x in input().split():
    x = int(x)
    if x == 0:
        break
    if x > z:
        z = x
print(z)
