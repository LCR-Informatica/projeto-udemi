# from sys import path
# from package99.modulo99 import soma_99, fala_oi # ou ***
# import package99.modulo99 # ou
# from package99 import modulo99
# from package99.modulo99 import * # pode usar com __all__ no modulo
# # from package99.modulo2 import fala_oi # ***

# # print(*path, sep='\n')
# # print('Principal: ', __name__)

# print(soma_99(2, 5)) # ou
# print(package99.modulo99.soma_99(4, 9)) # ou
# print(modulo99.soma_99(1, 4))
# print(nome, sobrenome) # acessado por * no import

# fala_oi()

# import package99
# print(package99.dobra(3))

from package99 import fala_oi, soma_99 # permitido pelo arquivo __init__.py

fala_oi()
print(soma_99(2, 5))