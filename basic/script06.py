l1 = int(input("Digite o lado 1: "))
l2 = int(input("Digite o lado 2: "))
l3 = int(input("Digite o lado 3: "))
if l1 == l2 and l1 == l3:
    print('O triângulo é equilátero.')
elif l1 != l2 and l1 != l3:
    print('O triângulo é escaleno.')
else:
    print('O triângulo é isósceles.')

