# Projeto - Chute um número
''''
O programa deve informar se o número chutado pelo usuário é maior ou menor que o número secreto.
# Método 5Q's para montar um algorítimo

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investique mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- valor aleatório de 1 a 10
- chute de um valor pelo usuário
2. O que devo fazer com estes dados?
- Eu devo comparar o chute do usuário com o valor aleatório que foi gerado no início do programa e dizer se o chute foi maior, menor ou igual ao valor que foi gerado no início do programa.
3. Quais são as restrições deste problema?
- Um valor aleatório entre 1 e 10
4. Qual é o resultado esperado?
- O resultado esparado é que o programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.
5. Qual é a sequencia de passos a ser feitas para chegar ao resultado esperado?
gere um valor aleatório inteiro entre 1 a 10 e armazene em valor_aleatorio
input chute do usuário e armazene em chute
if chute > valor_aleatorio
   print "Chute foi maior que o valor gerado!"
elif chute < valor_aleatorio
   print "Chute foi menor que o valor gerado!"
   if chute == valor_aleatorio
   print "Parabéns! Você acertou!"
'''
import random

valor_aleotorio = random.randint(1, 10)

acertou = False
while acertou == False:
    chute = int(input("Chute um número entre 1 e 10: "))
    if chute > valor_aleotorio:
        print(f'O Chute {chute} foi MAIOR que o valor gerado {valor_aleotorio}!')
    elif chute < valor_aleotorio:
       print(f'O Chute {chute} foi MENOR que o valor gerado {valor_aleotorio}!')
    if chute == valor_aleotorio:
        acertou = True
        print(f'PARABéNS! Você acertou! O valor {chute} do chute corresponde ao valor gerado {valor_aleotorio}!')