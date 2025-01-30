import re
digitado = input('Digite o CPF sem traço e pontos: ')
#cpf = cpf.replace('.', '').replace('-','').replace(' ','').replace(',','')
cpf = re.sub(r'[^0-9]','',digitado)
if digitado == (digitado[0] * len(digitado)):
    print('CPF digitado tem valores repetidos.')
else:    
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
    if cpf_final == cpf:
        print('CPF válido')
    else:
        print('CPF inválido')