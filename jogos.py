from random import randint
from time import sleep

def jogada (larg, limite, n_jogo, jogos, total):
    print('=' * larg)
    print(f'{n_jogo:^{larg}}')
    print('=' * larg)
    if jogos > 0:
        cartoes = []
        for n in range(jogos):
            lista = []
            c = 0
            while True:
                num = randint(1, limite) # define quantidade de números do jogo
                if num not in lista:
                    lista.append(num)
                    c += 1
                if c >= total: # define quantidade de números escolhidos
                    break
            lista.sort()
            cartoes.append(lista)
        for c, n in enumerate(cartoes):
            print(f'Jogo {c+1}:')
            print(f'Números: {n}')
            sleep(1)
    print('=' * larg)

jogos = int(input('Quantos cartões serão gerados? [0- cancela] '))
jogo = int(input('Qual jogo deseja? [1]-Mega Sena [2]-Loto Fácil [3]-Lotomania [4]-Quina '))
if jogo == 1:
    jogada (33, 60, "MEGA SENA", jogos, 6)
elif jogo == 2:
    jogada (70, 25, "LOTO FÁCIL", jogos, 15)
elif jogo == 3:
    jogada (140, 99, "LOTOMANIA", jogos, 50)
elif jogo == 4:
    jogada (30, 80, "QUINA", jogos, 5)
else:
    print('Escolha um jogo válido!')
