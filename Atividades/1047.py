hi,mi,hf,mf = [int(X) for X in input().split()]

total_h = hf-hi
total_m = mf-mi

if(total_h <=0) and (total_m <=0):
    total_h += 24
if (total_m < 0):
    total_m += 60
    total_h -= 1

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(total_h,total_m))