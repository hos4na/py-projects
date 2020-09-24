cod = input("Digite seu código: ")
qnt = int(input("Digite a quantidade de produtos: "))
pr = float(input("Digite o valor do produto: "))
fp = int(input("Digite 1 para dinheiro, 2 para cheque, 3 para débito, 4 para crédito: "))
vl = qnt * pr 
if fp == 1:
    desc = vl * 10 / 100
    vf = vl - desc
    print('O valor final é de R${}'.format(vf))
elif fp == 2:
    desc = vl * 2 / 100
    vf = vl - desc
    print('O valor final é de R${}'.format(vf))
elif fp == 3 or fp == 4:
    desc = vl * 5 / 100
    vf = vl - desc
    print('O valor final é de R${}'.format(vf))
