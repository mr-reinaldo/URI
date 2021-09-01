# Valor da linha
L = int(input())
# Caractere S (soma) ou M (Média) em maiusculo.
T = str(input()).upper()

# Matriz vazia
M = []

# Variavel para calculo da média.
media = 0.0
# criando a matriz[12][12] vazia.
for i in range(12):
    M.append([])

# Percorrendo a matriz -> M[linha][Coluna].
for i in range(12):
    for j in range(12):
        # ler um valor float.
        V = float(input())
        # anexa o valor a M[i][valor,...]
        M[i].append(V)

# se o caractere for 'S'.
if T == 'S':
    soma = 0
    # Pecorre os valores na linha informada no inicio M[L]
    for value in M[L]:
        # soma = soma + valores.
        soma += value
    print("{:.1f}".format(soma))
# se o caractere for 'M'.
if T == 'M':
    soma = 0
    # Pecorre os valores na linha informada no inicio M[L]
    for value in M[L]:
        # soma = soma + valores.
        soma += value
    # Media será a soma/tamanho da linha que é 12.
    media = soma/12
    print("{:.1f}".format(media))
