qtest = int(input())

C = R = S = 0

for i in range(1, qtest+1):
    qt,tipo = input().split()
    qt = int(qt)

    if(tipo == 'C'):
        C+=qt
    if(tipo == 'R'):
        R+=qt
    if(tipo == 'S'):
        S+=qt

total = (C+R+S)
perc_c = ((C/total)*100)
perc_r = ((R/total)*100)
perc_s = ((S/total)*100)

print("Total: {} cobaias\n\
Total de coelhos: {}\n\
Total de ratos: {}\n\
Total de sapos: {}\n\
Percentual de coelhos: {:.2f} %\n\
Percentual de ratos: {:.2f} %\n\
Percentual de sapos: {:.2f} %\
".format(total, C, R, S, perc_c, perc_r, perc_s))