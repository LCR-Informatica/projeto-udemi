# Falsy e Truthy
# Tipos mutáveis = [] {} set()
# Tipos imutaveis = () str in float range() bool None

lista = [0]
dicionario = {}
conjunto = set()
tupla = (1)
string = " "
inteiro = 1
decimal = 0.1
nada = None
boleano = False
intervalo = range(1)

def falsy(v):
    return 'falsy' if not v else 'truthy'

print(f'Teste', falsy('Teste'))
print(f'{lista = }', falsy(lista))
print(f'{dicionario = }', falsy(dicionario))
print(f'{conjunto = }', falsy(conjunto))
print(f'{tupla = }', falsy(tupla))
print(f'{string = }', falsy(string))
print(f'{inteiro = }', falsy(inteiro))
print(f'{decimal = }', falsy(decimal))
print(f'{nada = }', falsy(nada))
print(f'{boleano = }', falsy(boleano))
print(f'{intervalo = }', falsy(intervalo))
