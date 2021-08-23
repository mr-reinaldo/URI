# cria uma lista vazia A = [].
A = []
# em um range de 100.
for i in range(100):
    # O programa irá ler 100 valores float.
    x = float(input())

    # E adiciona o valor a lista: append() é a mesma coisa que -> A[i] = valor.
    A.append(x)
    # verifica se o valor de x é menor que 10.0.
    if (x <= 10.0):
        # caso verdadeiro irá printar no formato A[i] = x
        print('A[{}] = {}'.format(i, x))
