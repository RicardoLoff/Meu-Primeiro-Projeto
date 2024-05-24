# Condicionais
# if, elif e else
# Encontre o maior entre 2 números
'''
input primeiro_valor
input segundo_valor
if primieiro_valor > segundo_valor
    print primeiro_valor
else
    print segundo_valor
'''
primerio_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))
if primerio_valor > segundo_valor:
    print(f'O primeiro valor {primerio_valor} é maior que o segundo valor {segundo_valor}')
else:
    print(f'O segundo valor {segundo_valor} é maior que o primeiro valor {primerio_valor}')