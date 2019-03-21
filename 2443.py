a,b,c,d = map(int,input().split())
import fractions 
x = fractions.gcd(b,d)
mmc = (b*d)//x
w = (mmc*a)//b 
y = (mmc*c)//d
p = w+y 
q = fractions.gcd(mmc,p)
print(p//q,mmc//q)
