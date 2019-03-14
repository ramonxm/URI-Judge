L,D = input().split()
K,P = input().split()

L,D,K,P = int(L),int(D),int(K),int(P)


A = L*K + L//D*P

print(A)
