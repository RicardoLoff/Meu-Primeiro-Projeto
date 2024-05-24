# Exercício de Função

def verifica_multa(velocidade):
    velocidade_maxima = 80
    
    if velocidade <= velocidade_maxima:
        print('Nao levou multa')
    
    elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
        print('Levou multa leve')
    
    elif velocidade >= velocidade_maxima + 10 and velocidade <= velocidade_maxima + 20:
        print('Levou multa grave')
    
    elif velocidade > velocidade_maxima + 20:
        print('Levou multa gravissima')

verifica_multa(velocidade = int(input('Digite sua velocidade:  ')))