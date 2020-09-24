
atual = int(input("Digite o ano atual: "))
nasc = int(input("Digite o ano que você nasceu: "))
idade = atual - nasc
if idade < 16:
    print('Sua idade é {} anos, você não pode votar!'.format(idade))

elif idade > 16:
    print('Sua idade é {} anos, você é eleitor.'.format(idade))

