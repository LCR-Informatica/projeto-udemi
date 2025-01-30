# função lambda
# função comum, porém com uma linha e anônima

lista = [
    {'nome': 'Luiz', 'sobrenome': "Gomes"},
    {'nome': 'Cindia', 'sobrenome': 'Freitas'},
    {'nome': 'Claudia', 'sobrenome': 'Pinage'},
    {'nome': 'Thiago', 'sobrenome': 'Ferraz'},
    {'nome': 'Aline', 'sobrenome': 'Galvão'},
]

# lista = [4,5,6,4,2,10,1]
# lista.sort() # mexe na lista
# l1 = sorted(lista) # cria cópia rasa
# print(lista)

# def ordena(item):
#     print(item)
#     return item['sobrenome']

# lista.sort(key=ordena)
# print()
# for item in lista:
#     print(item)
    
    
# def exibir(lista):
#     for item in lista:
#         print(item)
#     print()

# l1 = sorted(lista, key=lambda item: item['nome'])
# l2 = sorted(lista, key=lambda item: item['sobrenome'])

# exibir(l1)
# exibir(l2)

## lamba mais avançado
def soma(x,y):
    return x+y

def executa(funcao, *args):
    return funcao(*args)


print(
    executa(lambda x,y: x+y , 2, 3), 
    executa(soma, 2,3), 
    soma(2,3)
)  ## fazem a mesma coisa

