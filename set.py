# Set são tipo de dados mutáveis que só aceitam dados imutaveis
# parecem dicionarios mas sem o par de chave/valor, somente valor
# não aceita valores repetidos
# são iteraveis (for, in, not in)
#  metodos
# add = inclui valor no set
# update = inclui valor iterado no set
# discart = discarta um valor do set
# clear = apaga todo o set

# s1 = set() # set vazio
# s2 = {'Luiz', 0, 1, 2} # set com dados
# s2.add('Paralelepipedo')
# print(s2)
# s2.clear()
# s2.update(('Paralelepipedo',1,2,3,4,5,6))
# print(s2)
# s2.discard('Paralelepipedo')
# print(s2)

# s1 = {1, 2, 3, 4}
# s2 = {2, 3, 4, 5, 6}
# s3 = s1 | s2 # union() unir
# s4 = s1 & s2 # intersection() interseção de valores presentes em ambos
# s5 = s2 - s1 # diference() mostra os itens não repetidos presentes somente no set da esquerda
# s6 = s1 ^ s2 # symetric_difference mostra itens que não estão em ambos

# print(s3, s4, s5, s6)

# letras = set()
# while True:
#     letra = input('Digite uma letra: ')[0].lower()
#     letras.add(letra)

#     if 'l' in letras:
#         print('Digitou l')
#         break
#     print(letras)