N = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

print(N)
for nota in notas:
    qtdn = N//nota
    print("{} nota(s) de R$ {},00".format(qtdn, nota))
    N -= qtdn*nota