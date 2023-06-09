numero = 0
try:
    numero = int(input('Digite um numero inteiro: '))
    if numero % 2 == 0:
        print('O número e par')
    else:
        print('O número é ímpar')
except:
    print('Não foi inserido um número inteiro')