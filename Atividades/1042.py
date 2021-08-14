A,B,C = [int(X) for X in input().split(" ")]

if (A > B > C ):
    print("{}\n{}\n{}\n\n{}\n{}\n{}".format(C,B,A,A,B,C))
elif (A > C > B ):
    print("{}\n{}\n{}\n\n{}\n{}\n{}".format(B,C,A,A,B,C))
elif (B > A > C ):
    print("{}\n{}\n{}\n\n{}\n{}\n{}".format(C,A,B,A,B,C))
elif (B > C > A ):
    print("{}\n{}\n{}\n\n{}\n{}\n{}".format(A,C,B,A,B,C))
elif (C > A > B ):
    print("{}\n{}\n{}\n\n{}\n{}\n{}".format(B,A,C,A,B,C))
elif (C > B > A ):
    print("{}\n{}\n{}\n\n{}\n{}\n{}".format(A,B,C,A,B,C))