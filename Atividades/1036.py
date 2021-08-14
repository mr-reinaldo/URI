
A, B, C = [float(V) for V in input().split()] 

D = (B**2)-4*A*C

if (A == 0) or (D <=0):
    print("Impossivel calcular")
else:
    R1 = (-B + D ** (1 / 2)) / (2 * A)
    R2 = (-B - D ** (1 / 2)) / (2 * A)
    
print("R1 = {:.5f}".format(R1))
print("R2 = {:.5f}".format(R2))