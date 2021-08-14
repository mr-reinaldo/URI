N = float(input())

NO = [100, 50, 20, 10, 5, 2]
MO = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")

for nt in NO:
    
    qtdn = int(N/nt)
    
    print("{} nota(s) de R$ {:.2f}".format(qtdn, nt))
    
    N -= qtdn*nt

print("MOEDAS:")

for mo in MO:

    qtdm = int(round(N,2)/mo)
    print("{} moeda(s) de R$ {:.2f}".format(qtdm, mo))
    N -= qtdm*mo