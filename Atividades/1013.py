A,B,C = [int(X) for X in input().split()]

maiorAB = int((A+B+abs(A-B))/2)

if maiorAB > C:
    print("{} eh o maior".format(maiorAB))
else:
    print("{} eh o maior".format(C))