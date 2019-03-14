L,A,P,R = input().split()
L,A,P,R = int(L), int(A), int(P), float(R)

R = R + R
D = ((L*L)+(A*A)+(P*P))**(1/2)

if (D <= R):
 print("S")
else:
    print("N")
