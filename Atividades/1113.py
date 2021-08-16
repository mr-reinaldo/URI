
#Lê os valores do usuário.
X,Y = input().split()
# Converte os valores de str -> int.
X,Y = int(X), int(Y)

'''
    Cria o laço de repetição, enquanto X for diferente de Y,
    e verifica as condições, se X for maior que Y ele é decrescente,
    se ele não for maior que Y ele é crescente.
'''

while (X != Y):
    
    if (X > Y):
        print("Decrescente")
    else:
        print("Crescente")

    #Lê os valores do usuário.
    X,Y = input().split()
    # Converte os valores de str -> int.
    X,Y = int(X), int(Y)