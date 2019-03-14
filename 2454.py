P,R = input().split()

P,R = int(P), int(R)

if P == 1 and R == 0:
  print("B")
elif P == 0 and R == 0:
  print("C")
elif P == 0 and R == 1:
  print("C")
elif P == 1 and R == 1:
  print("A")
