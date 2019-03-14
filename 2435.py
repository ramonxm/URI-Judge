N1,D1,V1 = input().split()
N2,D2,V2 = input().split()

N1,N2,D1,D2,V1,V2= int(N1), int(N2), int(D1), int(D2), int(V1), int(V2)

t1 = (D1) / V1
 
t2 = (D2) / V2
 
if (t1 < t2):
    print(N1)
else:
    print(N2)
