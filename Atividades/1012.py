A,B,C = [float(X) for X in input().split()]

# area do triangulo retangulo A=base C=altura.
atr = (A*C)/2
# área do círculo de raio C. (pi = 3.14159)
pi = 3.14159
acr = (pi*C**2)
# a área do trapézio que tem A e B por bases e C por altura.
atp = ((A+B)*C)/2
#  a área do quadrado que tem lado B.
aqd = (B**2)
# a área do retângulo que tem lados A e B.
art = (A*B)

print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(atr,acr,atp,aqd,art))