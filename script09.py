times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
'Cruzeiro', 'F L A M E N G O', 'Vasco', 'Chapecoense',
'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
'São Paulo', 'Fluminense', 'Sport Recife',
'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
'Atlético-GO')
print('_' * 90)
print(f'O MELHOR É: {times[5]}')
print('_' * 90)
print(f'Lista de times do Brasileirão: {times}')
print('_' * 90)
print(f'Os 5 primeiros são {times[0:5]}')
print('_' * 90)
print(f'Os 4 últimos são {times[-4:]}')
print('_' * 90)
print(f'Times em ordem alfabética: {sorted(times)}')
print('_' * 90)
print(f'O Chapecoense está na {times.index("Chapecoense")+1} a posição')
