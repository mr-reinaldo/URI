
# Criei um laço de repetição com loop infinito, enquato ele for verdeiro
# vai rodar sem parar.
while (True):
    # lê um valor do usuário.
    X = int(input())
    # se o valor de X for igual a 0, o break finaliza a interação do programa.
    # e parte para os proximos passos se tiver.
    if (X == 0):
        break
    # criei um lanço com -> for, que para cada valor no range de 1 à X+1,
    # ira executar as instruções logo em seguida.
    for i in range(1,X+1):
        # se o valor de -> i for igual ao valor de -> X.
        if (i == X):
        # sera impresso na tela o valor de -> i, com uma quebra de linha.
            print(i, end="\n")
        # se o valor de -> i for diferente de -> X, sera impresso na tela 
        # sem uma quebra de linha, mas com um espaço entre os valores ex: 1 2 4 ...
        else:
            print(i, end=" ")