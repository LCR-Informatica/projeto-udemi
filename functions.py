# def soma(x, y, z=None):
#     if z is not None:
#         print(f'{x=} {y=} {z=}', x + y + z)
#     else:
#         print(f'{x=} {y=}', x + y)

# soma(9,3)
# soma(19, 33)
# soma(7, 15, 0)


# def escopo():
#     x = 10
#     def outra():
#         x = 20
#         y = 5
#         print(x, y)
    
#     outra()
#     print(x)


# x = 2
# print(x)
# escopo()
# print(x)

# def produto(*args):
#     total = 1
#     for num in args:
#         total *= num
#     return total

# print(produto(2,3,4,5,6))

# def par_impar(num):
#     if num % 2 == 0:
#         return 'Numero é par'
#     return 'Numero é impar'

# print(par_impar(54))