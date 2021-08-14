C,Q = [int(X) for X in input().split(" ")]

if (C == 1):
    print("Total: R$ {:.2f}".format(Q*4.00))
elif (C == 2):
    print("Total: R$ {:.2f}".format(Q*4.50))
elif (C == 3):
    print("Total: R$ {:.2f}".format(Q*5.00))
elif (C == 4):
    print("Total: R$ {:.2f}".format(Q*2.00))
elif (C == 5):
    print("Total: R$ {:.2f}".format(Q*1.50))