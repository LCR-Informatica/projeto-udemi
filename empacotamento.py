# frase = 'O Python é uma linguagem de programação multiparadigma, Python foi criado por Guido Van Rossum'

# i = 0
# mais_vezes = 0
# letra_mais_vezes = ''
# while i < len(frase):
#     letra_atual = frase[i]
#     qtd_letra_atual = frase.count(letra_atual)
#     if letra_atual == ' ':
#         i += 1
#         continue
#     if mais_vezes < qtd_letra_atual:
#         mais_vezes = qtd_letra_atual
#         letra_mais_vezes = letra_atual
#     i += 1
# print(letra_mais_vezes, 'apareceu', mais_vezes, 'x vezes')

# numeros = range(10)
# for num in numeros:
#     print(num)

# texto = iter('luiz')    #.__iter__()  ## dander = __
# print(next(texto))  # .__next__()

# for letra in texto 
#     print(letra)

#texto = 'Luiz' # iteravel
#iterador = iter(texto) # iterador
#while True:  # faz isso por baixo dos panos
#    try:
#        letra = next(iterador)
#        print(letra)
#    except StopIteration:
#        break

# palavra secreta
# import os
# palavra_secreta   = 'fluminense'
# letras_certas = ''
# num_tentativas = 0
# while True:
#     num_tentativas += 1
#     letra = input('Digite a letra: ').lower()[0]
#     if letra in palavra_secreta:
#         letras_certas += letra
#     palavra_formada = ''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_certas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += '*'
#     print('Palavra formada:', palavra_formada)
#     if palavra_formada == palavra_secreta:
#         os.system('clear')
#         print(f'Voce acertou em {num_tentativas} tentativas.')
#         print('A palavra era:', palavra_secreta)
#         letras_certas = ''
#         num_tentativas = 0

# lista mutavel
# metodos uteis:
# append - add item ao final da lista
# insert - add item no index indicado
# pop - apaga o item no final ou no index indicado
# del - apaga um indice
# clear - limpa a lista
# extend - estende a lista
# + - concatena listas
# Create, read, update, delete
# lista1 = lista2 = apontam para o meso local na memória
#lista = [123, 'Luiz', True, 1.23, []]
#lista1 = [456, False, 'Luiz', 4.56]
#lista[1] = 'Maria'
#print(lista)
#lista2 = lista + lista1
#print(lista2)
#lista.extend(lista1)
#print(lista)

#lista = ['Luiz', 'Maria', 'Joao']
#indice = range(len(lista))
#for i in indice:
#    print(i, lista[i])

#l1, l2, l3 = lista # desempacotamento
#print(l1)

#_, l1, *resto = lista
#print(l1, resto)

# tuplas são como listas porem imutaveis

