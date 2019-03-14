A,B,C = input().split()
X,Y,Z = input().split()

A,B,C,X,Y,Z = int(A),int(B),int(C),int(X),int(Y),int(Z)


R = (X//A) * (Y//B) * (Z//C)

print(R)
