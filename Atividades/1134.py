# criei e iniciei os contadores com 0.
alcool = gasolina = diesel = 0 

# Criei um laço de repetição com loop infinito, enquato ele for verdeiro
# vai rodar sem parar.
while(True):
    # Lê o tipo de combustivel de 1-4 -> 1:alcool, 2:gasolina, 3:diesel, 4:finalizar.
    tipo_combustivel = int(input())
    # se o tipo for maior que 4 e menor que 1, será pedido outro valor ao usuário.
    if (tipo_combustivel > 4) and (tipo_combustivel < 1):
        tipo_combustivel = int(input())
    # se ele informa um valor dentro do [1,4].
    else:
    # se o tipo for igual a um dos tipos abaixo,cada contador somará 0+N,N+N,... para o tipo selecionado.
        if(tipo_combustivel == 1):
            alcool+=1
        elif(tipo_combustivel == 2):
            gasolina+=1
        elif(tipo_combustivel == 3):
            diesel+=1
    # Caso o usuário digite 4 o programa é finalizado.
        elif(tipo_combustivel == 4):
    # o -> break (para finalizar a execução da interação.)
            break
# ao finalizar a interação, são impressos os dados abaixo na tela:
print("MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}"
    .format(alcool, gasolina, diesel))