'''
Projeto - Medidor de Velocidade

Levando em consideração a velocidade máxima permitida de  80km em uma determinada rua. Crie um programa que recebe do usuário um valor que representa a velocidade e com base nessa velocidade informada avaliar e exibir mensagem que a pessoa  tomou uma multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velociade máxima seu programa deve exibir "não houve multa", caso esteja até 10 km acima, deve exibir: "levou multa leve",caso esteja entre 11 a 20 km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20 km da velocidade máxima, exiba: "levou multa gravíssima".
'''

# Método 5Q's para montar um algorítimo
'''
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investique mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- velocidade
2. O que devo fazer com estes dados?
- Deve comparar a velocidade recebida com a velociade máxima de 80 km/h e se a pessoa estiver abaixo da velociade máxima seu programa deve exibir "não houve multa", caso esteja até 10 km acima, deve exibir: "levou multa leve",caso esteja entre 11 a 20 km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20 km da velocidade máxima, exiba: "levou multa gravíssima".
3. Quais são as restrições deste problema?
- Não foi verificada alguma restrição
4. Qual é o resultado esperado?
- O resultado esperado é a exibição de mensagem levando em consideração se a velocidade do veículo da pessoa estiver abaixo da velociade máxima seu programa deve exibir "não houve multa", caso esteja até 10 km acima, deve exibir: "levou multa leve",caso esteja entre 11 a 20 km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20 km da velocidade máxima, exiba: "levou multa gravíssima".
5. Qual é a sequencia de passos a ser feitas para chegar ao resultado esperado?
input velocidade
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print "não houve multa"
if velocidade > velocidade_maxima e velocidade <= velocidade_maxima+10:
    print "levou multa leve"
if velocidade > velocidade_maxima+10 e velocidade <= velocidade_maxima+20:
    print "levou multa grave"
if velocidade > velocidade_maxima+20:
    print "levou multa gravíssima"
'''
velocidade = int(input('Digite a velocidade do veículo: '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print('Não levou multa.')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima+10:
    print('Levou multa leve!')
elif velocidade > velocidade_maxima+10 and velocidade <= velocidade_maxima+20:
    print('Levou multa grave!!')
else: # velocidade > velocidade_maxima+20
    print('Levou multa gravíssima!!!')