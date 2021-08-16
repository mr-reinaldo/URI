# iniciei a váriavel ng com o valor 1, sendo assim o programa já iniciara.
ng = 1

# criei 4 contadores para os grenais, empate, vitorias do inter e do gremio.
count_grenais = 0
count_empate = 0
count_vinter = 0
count_vgremio = 0

'''
    criei um laço de repetição, equanto o variavel -> ng, for igual a 1,
    o laço continuara, quando a variavel -> ng for igual a 2 o laço sera finalizado.
'''
while (ng == 1):
    # ler a quantidade de gol na rodada.
    inter,gremio = [int(X) for X in input().split()]
    
    # se a quantidade de gol do inter for igual a do gremio, será impate.
    if (inter == gremio):
    # o contador somará 0+N, N+N,...
        count_empate+=1
    # se o quantidade de gols do inter for maior que a do gremio.
    if (inter > gremio):
    # o contador de vitorias do inter somará 0+N, N+N,...
        count_vinter+=1
    # se a quantidade de gosl do inter for menor que a do gremio.
    else:
    # contador de vitorias do gremio somará 0+N, N+N,...
        count_vgremio+=1
    
    # conta de grenais, a cada novo grenal o contador somará 0+N, N+N,...
    count_grenais+=1
    # será perguntado ao usuário se ele quer gerar um novo grenal
    # se ele digitar 2 o laço será incerrado, se digitar 1 o laço continuará.
    ng = int(input('Novo grenal (1-sim 2-nao)'))

# quando o laço for finalizado sera impresso na tela, os resultados abaixo:
print("{} grenais\nInter:{}\nGremio:{}\nEmpates:{}"
    .format(count_grenais, count_vinter, count_vgremio, count_empate))

# se a quantidade de vitorias por rodadas do inter for maior que a do gremio, inter venceu mais.
if ( count_vinter > count_vgremio):
    print("Inter venceu mais")
# se a quantidade de vitorias por rodadas do gremio for maior que a do inter, gremio venceu mais.
elif(count_vinter < count_vgremio):
    print("Gremio venceu mais")
# se não vitorias, de ambas as equipes, não houve vencedor.
else:
    print("Nao houve vencedor")