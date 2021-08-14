valores = input().split()
valores = map(float,valores)

A,B,C = sorted(valores,reverse=True)

if (A >= (B + C)):
    print("NAO FORMA TRIANGULO")
else: 
    if ((A**2) == (B**2 + C**2)):
        print("TRIANGULO RETANGULO")
    if ((A**2) > (B**2 + C**2)):
        print("TRIANGULO OBTUSANGULO")
    if ((A**2) < (B**2 + C**2)):
        print("TRIANGULO ACUTANGULO")
    if (A == B == C):
        print("TRIANGULO EQUILATERO")
    if (A == B != C) or (B == C != A) or (A == C != B):
        print("TRIANGULO ISOSCELES")