plug1 = input().split()
plug2 = input().split()
conta = 0
for i in range(5):
    if plug1[i] != plug2[i]: 
        conta += 1  
if conta == 5: 
    print("Y")
else:
    print("N")
