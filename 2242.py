data = input()
vogais = []
for char in data:
    if char in ["a", "e", "i", "o", "u"]:
        vogais.append(char)
if vogais == vogais[::-1]:  
    print("S")
else:
    print("N")
