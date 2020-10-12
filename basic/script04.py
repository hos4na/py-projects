nome = input("Digite seu nome: ")
n1 = float(input("Digite sua nota 1: "))
n2 = float(input("Digite sua nota 2: "))
media = n1 + n2
if media < 7:
    print('Sua média é {}. REPROVADO!'.format(media))
elif media > 7:
    print('Sua média é {}. APROVADO!'.format(media))
