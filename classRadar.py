# CamelCase
class Radar:
  def __init__(self,velocidade_maxima,multa_leve,multa_grave,multa_gravissima):
    self.velocidade_maxima = velocidade_maxima
    self.multa_leve = multa_leve
    self.multa_grave = multa_grave
    self.multa_gravissima = multa_gravissima

# A função deve exibir o valor da multa que será aplicad, de acordo com o nível da multa
  def obter_valor_multa(self,nivel_multa):
    if nivel_multa == 'multa leve':
      print(f'O valor da multa leve é R${self.multa_leve}')
    elif nivel_multa == 'multa grave':
      print(f'O valor da multa grave é R${self.multa_grave}')
    else:
      print(f'O valor da multa gravissima é R${self.multa_gravissima}')

  def calcular_multa(self,velocidade):
    if velocidade <= self.velocidade_maxima:
        print('Nao levou multa')

    elif velocidade > self.velocidade_maxima and velocidade <= self.velocidade_maxima + 10:
        print('Levou multa leve')

    elif velocidade >= self.velocidade_maxima + 10 and velocidade <= self.velocidade_maxima + 20:
        print('Levou multa grave')

    elif velocidade > self.velocidade_maxima + 20:
        print('Levou multa gravissima')

  def aplicar_penalizacao_carteira(self,nivel_multa):
    if nivel_multa == 'Multa leve':
      print('Perdeu 3 pontos na carteira')

    elif nivel_multa == 'Multa grave':
      print('Perdeu 5 pontos na carteira')

    else:
      print('Perdeu 7 pontos na carteira')


radar1 = Radar(velocidade_maxima=80,multa_leve=90,multa_grave=100,multa_gravissima=110)
# print(radar1.velocidade_maxima)
# radar1.obter_valor_multa('multa gravissima')
# radar1.calcular_multa(101)
radar1.aplicar_penalizacao_carteira(nivel_multa='Multa leve')