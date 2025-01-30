from struct import unpack

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if nome and idade :
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome :
        print(f'Seu nome contém espaço')
    else :
        print(f'Seu nome não contém espaço')
    print(f'Seu tem {len(nome)} letras')
    print(f'A primeira letra é {nome[0]}')
    print(f'A última letra é {nome[-1]}')
else :
    print('Você deixou campos vazios!')