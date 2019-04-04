quantidade = int(input())
broken = 0

while quantidade > 0:
    l, c = map(int, input().split())
    quantidade = quantidade - 1
    if l > c:
        broken += c

print(broken)
