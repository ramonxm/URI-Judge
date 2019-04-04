vezes = int(input())
q = 0
while vezes > 0:
    vezes -= 1
    N = int(input())
    if N > 1:
        q += 1
    else:
        continue
print(q)
