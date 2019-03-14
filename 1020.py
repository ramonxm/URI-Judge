N = int(input())

A=N//365

M=(N%365)//30

D=(N%365)%30

print(A,"ano(s)")
print(M,"mes(es)")
print(D,"dia(s)")
