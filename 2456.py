A,B,C,D,E = input().split()

A,B,C,D,E = int(A),int(B),int(C),int(D),int(E)

if A < B < C < D < E:
    print ("C")
elif A > B > C > D > E:
    print ("D")
else:
    print("N")
