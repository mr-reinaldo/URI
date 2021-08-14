par=impar=pos=neg=0

for i in range(5):
    valores = float(input())
    if(valores > 0):
        pos+=1
    if(valores < 0):
        neg+=1
    if(valores%2==0):
        par+=1
    if(valores%2!= 0):
        impar+=1
    

print("{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)"
    .format(par,impar,pos,neg))