cd1, np1, vu1 = input().split()
cd2, np2, vu2 = input().split()

cd1, np1, vu1 = int(cd1), int(np1), float(vu1)
cd2, np2, vu2 = int(cd2), int(np2), float(vu2)

ttp = ((np1*vu1)+(np2*vu2))
print("VALOR A PAGAR: R$ {:.2f}".format(ttp))

