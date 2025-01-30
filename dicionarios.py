import copy

pessoas = {
    'nome': 'Luiz Alberto',
    'sobrenome': 'Gomes',
    'idade': 57,
    'altura': 1.71,
    'telefones' : [
        { 'ddd': '22', 'numero': '998117257'},
        { 'ddd': '22', 'numero': '41050545'}
    ],
    'enderecos': [
        {'rua': 'Leonino Dutra', 'numero': '336', 'bairro': 'Varginha'},
        {'rua': 'Euterpe friburguense', 'numero': '33', 'bairro': 'Centro'}
    ]
}

# for chave in pessoas:
#     if type(pessoas[chave]) is list:
#         print(chave + ': ')
#         print(end='')
#         for dados in pessoas[chave]:
#             if type(dados) is dict:
#                 print('    ', end='')
#                 for info in dados:
#                     print(dados[info]+', ' ,end='')
#             print()
#     else:
#         print(chave + ':', pessoas[chave])

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2]
}

# d2 = d1 # aponta para mesma posição na memória 
# d2 = copy.copy(d1) # idem acima
# d2 = d1.copy() # copia somente dados IMUTAVEIS, o restante fica como referencia de memoria
# d2 = copy.deepcopy(d1) # muito consumo de memória

# d2['c1'] = 99
# d2['l1'][1] = 8888

# print(d1)
# print(d2)

p1 = {
    'nome': 'Luiz Alberto',
    'sobrenome': 'Gomes',
    'idade': 57,
}

# print(p1.get('altura', 'retorna bool ou Não existe'))
# nome = p1.pop('nome')
# print(nome)
# print(p1.get('nome'))
ultimo_valor = p1.popitem()
print(ultimo_valor)
print(p1)
print
# p1.update({
#     'idade': 56,
#     'altura': 171
# }) # ou
# p1.update(idade=57, altura=172) # ou
lista = [['idade', 58],['altura', 173]]
p1.update(lista)
print(p1)
