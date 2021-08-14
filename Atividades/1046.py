Hi,Hf = [int(X) for X in input().split(" ")]

if(Hi > Hf): 
    
    print("O JOGO DUROU {} HORA(S)".format(24-(Hi-Hf)))

elif(Hf > Hi):
    print("O JOGO DUROU {} HORA(S)".format(Hf-Hi))

else:
    print("O JOGO DUROU 24 HORA(S)")
