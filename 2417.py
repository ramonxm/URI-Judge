Cv,Ce,Cs,Fv,Fe,Fs = input().split()
Cv,Ce,Cs,Fv,Fe,Fs = int(Cv),int(Ce),int(Cs),int(Fv),int(Fe),int(Fs)

A = 3*Cv + Ce
B = 3*Fv + Fe

if A > B:
    print("C")
elif B > A: 
    print("F")
elif A == B:
    if Cs > Fs:
        print ('C')
    elif Fs > Cs:
        print('F')
    elif Cs == Fs:
        print("=")
