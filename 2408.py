A,B,C = input().split()

A,B,C = int(A),int(B),int(C)

if (A > B and A < C) or (A > C and A < B):
    print (A)
elif (B > A and B < C) or (B > C and B < A):
    print (B)
else:
    print (C)
