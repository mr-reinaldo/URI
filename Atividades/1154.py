# criei 2 variaveis, media e count(contador), e iniciei as duas com 0.
media = count = 0

# Criei um laço de repetição com loop infinito, enquato ele for verdeiro
# vai rodar sem parar.
while (True):
    # lê um valor inteiro que o usuário digitar.
    idade = int(input())
    # se a idade digitado for meno que 0, a interação do codigo finalizará
    # e se houver instruções em seguida do laço, será executada.
    if (idade < 0):
        break
    # caso a idade seja maior que 0, somará a media que foi iniciada com 0 + idade.
    else: 
        media += idade
    # o contador que foi iniciado com 0, sera somado com + 1, N+N... assim por diante,
    # ele servirá para contar quantas idades foram informadas pelo usuário.
        count+=1
# imprime na tela com 2 casas decimais, a media dividido pela quantidade de idades informadas.
print("{:.2f}".format(media/count))