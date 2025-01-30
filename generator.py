# generator expression, Iterables e Iterators em Python
# import sys

# iterable = ['Eu', 'tenho', '__iter__']
# iterator = iter(iterable) # __iter__ e __next__
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print()

# lista = [x for x in range(1000)]
# print(sys.getsizeof(lista))

# generator = (x for x in range(1000))
# print(sys.getsizeof(generator))
# for x in generator:
#     print(x)
    
## generation function

# def generator(n=0, maximum=10):
#     while True:
#         yield n
#         n += 1
#         if n >= maximum:
#             return

# gen = generator(maximum=1000)
# for n in gen:
#     print(n)

# yield from

def gen1():
    print('Iniciou Gen1')
    yield 1
    yield 2
    yield 3
    print('Terminou Gen1')
    
def gen2(gen=None):
    print('Iniciou Gen2')
    if gen is not None:
        yield from gen()
    yield 4
    yield 5
    yield 6
    print('Terminou Gen2')
    
def gen3():
    print('Iniciou Gen3')
    yield 7
    yield 8
    yield 9
    print('Terminou Gen3')
    
g1 = gen2(gen1)
g3 = gen2(gen3)
g2 = gen2()

for n in g1:
    print(n)
print()    
for n in g3:
    print(n)
print()
for n in g2:
    print(n)
print()