# List comprehention
# é uma forma rapida de criar listas 
# a partir de iteráveis

# print(list(range(10)))

# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

# lista = [ numero for numero in range(10) if numero < 5]
# print(lista)

# mapeamento de lista com list comprehention
# a esquerda do for é mapeamento
# a direita é filtro

# produtos = [
#     {'nome': 'Prod01', 'preco': 10,},
#     {'nome': 'Prod02', 'preco': 20,},
#     {'nome': 'Prod03', 'preco': 30,},
#     {'nome': 'Prod04', 'preco': 40,},
# ]

# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
#     if produto['preco'] > 10
# ]
# print(*novos_produtos, sep='\n')

# for dentro de for
# lista = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x,y))
        
lista = [
    [(x,y) for x in range(3)]
    for y in range(3)
]
print(lista)