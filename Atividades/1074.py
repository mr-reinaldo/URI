# Vai ler a quantidade de testes em inteiro que o *for irá rodar. 
N = int(input())

# para *i em range(*N) de tamanho *N.
for i in range(N):
    # leia um valor inteiro.
    X = int(input())
    # verifica se X é igual a 0, se X for igual a 0 print("NULL").
    if (X == 0):
        print("NULL")
    else:
     # se X não for igual a 0, e verifica se o resto da divisão de X por 2 é igual a 0, se for ele é par.
        if(X%2 == 0):
            # se o resto da divisão de X for igual a 0 e se for maior que 0 ele é par positivo. 
            if (X > 0):
                print("EVEN POSITIVE")
            # caso contrario X for menor que 0 ele é par negativo.
            else:
                print("EVEN NEGATIVE")
        # se o resto da divisão de X por 2 for diferente de 0, ele é impar.
        else:
            # se for mair que 0, ele é um impar positivo.
            if(X > 0):
                print("ODD POSITIVE")
            # caso contrario X menor que 0 ele é um impar negativo.
            else:
                print("ODD NEGATIVE")
