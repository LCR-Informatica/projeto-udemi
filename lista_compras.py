# from time import sleep
# import os
# compras = []

# def erro(msg):
#     print(msg)
#     sleep(1)
#     os.system('clear')

# while True:
#     opcao = input('''Selecione uma opção 
# [i]nserir [a]pagar [l]istar [s]air: ''').lower()[0]
#     if opcao == 's':
#         break
#     elif opcao == 'i':
#         os.system('clear')
#         item = input('Digite o item da lista: ')
#         compras.append(item)
#     elif opcao == 'a':
#         item = int(input('Digite o número do item: ')[0])
#         try: 
#             compras.pop(item)
#         except ValueError:
#             erro('Digite um numero inteiro!')
#         except IndexError:
#             erro('Indice não existente.')
#         except Exception:
#             erro('Erro desconhecido!')
#     elif opcao == 'l':
#         os.system('clear')
#         for i, n in enumerate(compras):
#             print(i, n)
#     else:
#         erro('Opção inválida!')
# print('Fim')

# frase = "    Olha só, que coisa interessante.     "
# print(frase.split())
# frase2 = frase.split(',')
# lista = []
# for i,parte in enumerate(frase2):
#     lista.append(frase2[i].strip())
# print(lista)

# filas = [['Maira', 'Helena'],
#          ['Elaine'],
#          ['Luiz', 'João','Pedro',(0,1,2,3,4)]]

# for k,fila in enumerate(filas):
#     for i,item in enumerate(fila):
#         if k == len(filas)-1 and i == len(fila)-1:
#             for num in item:
#                 print(num)
#         else:
#             print(k, i, item)

# print(*filas, sep='\n')
# p, *_, u = filas
# print(p, u)

# operador ternario
# <valor> if <condição> else <senão>
# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'Outro Valor'
# print(variavel)
# <valor> if <condicao> else <outro valor> if <condicao> <valor final>
