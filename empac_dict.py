# Empacotamento de desempacotamento de dicionários
# empacotar poe coisas no dicionario
# desempacotar tira coisas do dicinario
# a, b = 1, 2
# print(a, b)
# a, b = b, a
# print(a, b) # aqui com tuplas

pessoa = { 
    'nome': 'Luiz', 
    'sobrenome': 'Gomes'
}
# a, b = pessoa
# print(a, b)
# a, b = pessoa.values()
# print(a, b)
# a, b = pessoa.items()
# print(a, b)
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2, b1, b2)

dados_pessoa = {
    'idade': 67,
    'altuta': 1.72
}

pessoa_completo = {**pessoa, **dados_pessoa}
print(pessoa_completo)

def mostro_argumentos_nomeados(*args, **kwargs):
  print('Args: ', args)
  
  for chave, valor in kwargs.items():
    print(chave, valor)
    
mostro_argumentos_nomeados(1,2,3, **pessoa_completo)