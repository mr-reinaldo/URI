# Caractere S (soma) ou M (Média) em maiusculo.
o = input().upper()
# Matriz vazia
M = []
# Percorrendo a matriz -> M[linha][Coluna].
for i in range(12):
    # lista vazia, referente a linha.
    L = []
    for j in range(12):
        # ler um valor float.
        V = float(input())
        # anexa o valor em L -> [Valor,...]
        L.append(V)
    # anexa L em M -> M[[Valor,...],...]
    M.append(L)

soma = 0
# se o caractere for 'S'.
if o == 'S':
    # Pecorre os valores nas Linhas e Colunas M[i][j]
    for i in range(12):
        for j in range(12):
            # se o indice 'i'(coluna) for maior que o indice 'j'(linha).
            if i > j:
                # soma = soma + M[i][valores]
                soma += M[i][j]
    print("{:.1f}".format(soma))

soma = 0
# se o caractere for 'M'.
if o == 'M':
    # Pecorre os valores nas Linhas e Colunas M[i][j]
    for i in range(12):
        for j in range(12):
            # se o indice 'i'(coluna) for maior que o indice 'j'(linha).
            if i > j:
                # soma = soma + M[i][valores]
                soma += M[i][j]
    # media = soma/((144-12)/2)
    media = soma/66
    print("{:.1f}".format(media))
