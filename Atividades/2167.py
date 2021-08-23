# quantidade de testes do motor.
N = int(input())

# Lista para receber o numero de rpm.
Ri = []

# Variável que ira contar as quedas de velocidade.
quedav = 0
# leitura dos valores de rpm.
Ri = input().split()

# para cada valor dentro da lista Ri, será convertido para inteiro.
Ri = [int(valor) for valor in Ri]

# para o range de 1 a N.
for i in range(1, N):
    # se o valor de Ri[i-1] ex: Ri[1-1] que irá pegar o valor do indice 0.
    # se esse valor for maior que Ri[i] ex: Ri[0] > Ri[1].
    if (Ri[i-1] > Ri[i]):
        # queda de velocidade recebe i + 1, indicando qual o valor do indice
        # que obteve a primeira queda de velocidade e depois para a repetição.
        quedav = i+1
        break
# printa saida.
print("{}".format(quedav))
