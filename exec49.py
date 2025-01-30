num_str = input('Digite um número: ')

try :
    print('Str: ',num_str)
    num_float = float(num_str)
    print('Float: ', num_float)
    print(f'O dobro de {num_str} é {num_float * 2}')
except :
    print('Isso não é um número.')