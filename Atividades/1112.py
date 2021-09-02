"""
    P = quantidade de peças.
    T = Tamanho do tabuleiro.

"""
P = int(input())
T = int(input())
"""
    remove -> Contador de peças removidas
    tabuleiro -> matriz.

"""
remove = 0
tabuleiro = []

"""
    Criando uma matriz[P][T]

    [[0,0,0,0],[0,0,0,0],...]
"""
for i in range(P):
    tabuleiro.append([0]*T)

for i in range(P):
    """
    Recebendo 2 valores usando compreensão de lista.

        * l,c = [int(x) for x in input().split()]

        * c = [v1,v2] -> l = v1 e c = v2

    """
    l, c = [int(x) for x in input().split()]

    """
        * Se o tabuleiro na linha 'l' e coluna 'c' for
    igual a 0, o tabuleiro[l][c] vai reber 1 peça.

        * Caso o tabuleiro na linha 'l' e coluna 'c' for
    diferente de 0, a significa que já existe uma peça
    nesta linha e coluna da matriz então ela sera removida.
    """
    if(tabuleiro[l][c] == 0):
        tabuleiro[l][c] = 1
    else:
        remove += 1
"""
    * Se a quantidade de peças removidas for maior que 0
o jogo retornara False e a quantidade de peças removidas,
e o partida não iniciará.

    * Caso não ocorrá a remoção de peças o jogo retornara
True e a quantidade de peças removidas == 0, e o partida
não iniciará.
"""
if remove > 0:
    print("{}\n{}".format(False, remove))
else:
    print("{}\n{}".format(True, remove))
