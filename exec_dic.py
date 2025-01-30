perguntas = [
    { 
        'Pergunta': 'Quanto é 2+2?',
        'Opções' : ['2','3','4','5'],
        'Resposta': '4',
    },
    { 
        'Pergunta': 'Quanto é 5*5?',
        'Opções' : ['25','35','45','55'],
        'Resposta': '25',
    },
    { 
        'Pergunta': 'Quanto é 10/2?',
        'Opções' : ['10','0','2','5'],
        'Resposta': '5',
    },
]
# resp = False
# for indice in perguntas:
#     for parte in indice.items():
#         if type(parte[1]) is list:
#             print(parte[0])
#             for opt,pte in enumerate(parte[1]):
#                 print(opt, ')', pte)
#             resp = input('Escolha : ')
#             r2 = parte[1][int(resp)]
            
#         else:    
#             print(parte[0]+' :',parte[1])
#             if resp:
#                 #print(r2, parte[1])
#                 if parte[1] == r2:
#                     print('Acertou!')
#                 else:
#                     print('Errou!')
#                 resp = False
#     print()
# ou

acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})',opcao)
    print()

    escolha = input('Escolha uma opção: ')

    escolha_int = None
    acertou = False
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    
    print()
    if acertou:
        print('Acertou')
        acertos += 1
    else:
        print('Errou')

print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')