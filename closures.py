'''
Closures e funções que retornam funções
programação funcional **
'''

# def criar_saudacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}'
#     return saudar

# falar_bom_dia = criar_saudacao('bom dia')
# falar_boa_noite = criar_saudacao('boa noite')

# nomes = ['Luiz', 'Cindia', 'Leora']
# for nome in nomes:
#     print(falar_bom_dia(nome))
#     print(falar_boa_noite(nome))

# def duplica(num):
#     return num * 2

# def tripica(num):
#     return num * 3

# def quadriplica(num):
#     return num * 4

def multiplicador(multiplo):
    def multiplicar(num):
        return multiplo * num
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)
...
print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

