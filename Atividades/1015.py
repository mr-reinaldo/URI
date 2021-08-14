import math
X1,Y1 = [float(X) for X in input().split()]
X2,Y2 = [float(X) for X in input().split()]

distancia = math.sqrt((X2-X1)**2+(Y2-Y1)**2)

print("{:.4f}".format(distancia))
