# cria uma variavel contador igual a 0.
count = 0

#Cria uma variavel media igual a 0.
media = 0

# cria um laço de repetição enquanto contador for menor que 2
# ele vericar as condições abaixo.

while (count < 2):

    # Lê os um valor float do usuario.
    nota = float(input())
    
    # se a nota for menor que 0,ou , a nota for maior que 10, a nota será invalida. 
    if(nota < 0) or (nota > 10):
        print("nota invalida")
    # se não, se a nota for maior ou igual a 0, ou a nota menor igual a 10.
    elif(nota >= 0 ) or (nota <= 10):
        # o contador soma 0+1, 1+N... e assim por diante.
        count+=1
        # a media soma 0 + nota, 0+N..., N+N...
        media += nota

# Imprime o resultado na tela, com duas casa decimais, ex: 7,85.
print("media = {:.2f}".format(media/2))