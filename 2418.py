N1,N2,N3,N4,N5 = input().split()
N1,N2,N3,N4,N5 = float(N1), float(N2), float(N3), float(N4), float(N5)

A = min(N1,N2,N3,N4,N5)
B = max(N1,N2,N3,N4,N5)

print('{:.1f}'.format(N1+N2+N3+N4+N5-A-B))
