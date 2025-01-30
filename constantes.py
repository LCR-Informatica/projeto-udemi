'''
CONSTANTE = Variaveis que não vão mudar
Muitas condições no mesmo if (ruim)
   <- contagem de complexidade (ruim)
'''

velocidade = 60 # valocidade do carro
km_carro = 100 # posição do carro na estrada

LIMITE_R1 = 60 # limite velocidade radar 1
LOCAL_R1 = 100 # km posicão radar 1
RANGE_R1 = 1   # range de atuação do radar (+ e -)

carro_excedeu_limite = velocidade > LIMITE_R1
carro_passou_no_radar1 = km_carro >= (LOCAL_R1 - RANGE_R1) and km_carro <= (LOCAL_R1 + RANGE_R1)
carro_multado_radar1 = carro_passou_no_radar1 and \
    carro_excedeu_limite

if carro_excedeu_limite:
    print('Carro excedeu velocidade em R1')

if carro_passou_no_radar1:
    print('Carro passou no R1')

if carro_multado_radar1:
    print('Carro multado em R1')