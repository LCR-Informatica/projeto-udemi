# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def divide(n, d):
    return n / d
    
    
def retornaErro(erro):
    print(f'Msg: {erro}')
    print(f'Erro: {erro.__class__.__name__}')

    return True
     
          
try:
    print('abrir arquivo')
    a = 120
    b = 2
    c = divide(a, b)
    # print(b[0])
    # print('erros'[10])
    print(c)

except Exception as erro:
    retornaErro(erro)

finally:
    print('fechar arquivo') # sempre é executado após o try
    
print('Fim')

# edição pelo github
