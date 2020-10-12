
listanum = []
maior = 0
menor = 0
for h in range(0, 5):
   listanum.append(int(input(f'Digite um valor para a Posição {h}: ')))
   if h == 0 :
       maior = menor = listanum[h]
   else:
       if listanum[h] > maior :
           maior = listanum[h]
       if listanum[h] < menor:
           menor = listanum[h]
print('-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior}', end=' ' '\n')
print(f'O menor valor digitado foi {menor}', end=' ')


