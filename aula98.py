import modulo98 # singleton (só uma vez)

import importlib

print(modulo98.variavel)

for i in range(10):
    print(i)
    importlib.reload(modulo98) # permite recarregar o modulo
    
print('FIM')