# Variáveis
# Números
velocidade_internet = 10
print(velocidade_internet)
nota_filme = 8.5 # float
# Valores booleanos
esta_aberto = True
esta_fechado = False
# Strings
nome_do_curso = 'Lógica de Programação'
# Como variáveis seriam usadas em um programa real?
# Probema 1 - Valor por hora
# Escreva um programa que retrona o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.
'''
input salario_mensal
input horas_trabalhadas_por_mes
valor_hora = salario_mensal / horas_trabalhadas_por_mes
print valor_hora
'''
salario_mensal = input('Qual o seu salário mensal? ')
horas_trabalhadas_por_mes = input('Quantas horas você trabalha por mês? ')
valor_hora = float(salario_mensal) / float(horas_trabalhadas_por_mes)
print('O valor da sua hora é: R$', valor_hora)
# Probema 2 - Valor por hora
# Escreva um programa que retrona o valor hora de
