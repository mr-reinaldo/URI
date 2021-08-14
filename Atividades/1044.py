#A,B = [int(X) for X in input().split()]
A,B = input().split()

A,B = int(A), int(B)


if (B%A == 0) or (A%B == 0):
    print("Sao Multiplos")
else:
   print("Nao sao Multiplos")