import random, sys 

cpf = ''
for i in range(9):
    cpf += str(random.randint(0,9))
print(cpf)

soma_result = 0
p = 0
for a in range(10,1,-1):
    digito = int(cpf[p]) * a
    p += 1
    soma_result += digito
    #print(digito, soma_result, a, p)
dig1 = (soma_result * 10) % 11
digito = 0 if dig1 > 9 else dig1
print(digito)

cpf += str(digito)
cpf2 = cpf[:9]+str(digito)

soma_result = 0
p = 0
for a in range(11,1,-1):
    digito = int(cpf[p]) * a
    p += 1
    soma_result += digito
    #print(digito, soma_result, a, p)
dig1 = (soma_result * 10) % 11
digito = 0 if dig1 > 9 else dig1
print(digito)

cpf_final = cpf2 + str(digito)

print(cpf_final)