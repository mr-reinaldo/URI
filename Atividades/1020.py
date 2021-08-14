q_dias = int(input())

ano = q_dias//365
mes = (q_dias%365)//30
dia = (q_dias%365)%30

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(ano, mes, dia))