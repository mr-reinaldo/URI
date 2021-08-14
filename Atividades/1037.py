valor = float(input())

if (valor < 0) or (valor > 100.0):
    print("Fora de intervalo")
elif ( valor <= 25.0):
    print("Intervalo [0,25]")
elif (valor <= 50.0):
    print("Intervalo (25,50]")
elif (valor <= 75.0):
    print("Intervalo (50,75]")
elif (valor <= 100.0):
    print("Intervalo (75,100]")