x = 2019
a,b,c = map(int,input().split())

m = x-a+b
n = x-a+c
o = x-b+c
p = x+a-b
q = x+a-b
r = x+a-b
s = x-a-b+c
t = x-a-c+b
u = x-b-c+a
v = x+a+b-c
w = x+a+c-b
z = x+b+c-a


if m == x or n == x or o == x or p ==x or q==x or r == x or s== x or t == x or u == x or v ==x or w==x or z == x:
    print("S")

else:
    print("N")
