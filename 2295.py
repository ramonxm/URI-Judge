A,G,RA,RG = input().split ()
A,G,RA,RG = float(A),float(G),float(RA),float(RG)

if RA/A > RG/G:
    print("A")
else:
    print("G")
