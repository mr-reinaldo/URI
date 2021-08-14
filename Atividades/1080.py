
posi = 0
mvalor = 0

for i in range(1, 5+1):
    number = int(input())
    
    if( number > mvalor):
        mvalor = number
        posi = i

print("{}\n{}".format(mvalor, posi))



