# ler o tamanho da lista.
N = int(input())

count = 0
posi = 0

X = input().split()
# Converte os valores de cada indece para inteiro.
X = [int(valor) for valor in X]

# Pega o indice 0 como menor valor.
menor = X[0]

# Percorre os valores da lista.
for valor in X:
    # se o valor X[i] for menor que menor.
    if(valor < menor):
        # menor = valor.
        menor = valor
        # posição recebe o valor do contador.
        posi = count
    # depois de executar a condição do if, o contador auto incremeta +1.
    count += 1

# printa saida.
print("Menor valor: {}\nPosicao: {}".format(menor, posi))
