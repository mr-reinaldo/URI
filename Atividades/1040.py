N1,N2,N3,N4 = [float(X) for X in input().split()]

MEDIA = ((N1*2)+(N2*3)+(N3*4)+N4)/10

print("Media: {:.1f}".format(MEDIA))

if (MEDIA >= 7.0):

    print("Aluno aprovado.")

elif(MEDIA < 5.0):
    
    print("Aluno reprovado.")

elif(MEDIA >= 5.0 and MEDIA <= 6.9):
    
    print("Aluno em exame.")
    
    NE = float(input())
    
    print("Nota do exame: {}".format(NE))
    
    if(((NE + MEDIA)/2.0) > 5.0): 
    
        print("Aluno aprovado.")
    
    else:
    
        print("Aluno reprovado.")
    
    print("Media final: {:.1f}".format(((NE + MEDIA)/2.0)))

else:
    print("Aluno aprovado.")
