count = total = 0

for i in range(6):
    valores = float(input())
    
    if(valores > 0):
        count+=1
        total += valores

print("{} valores positivos\n{:.1f}".format(count,(total/count)))