nome = 'Igor'
peso = 119.0
altura = 1.90

imc = peso / (altura ** 2)

print(f'{nome} tem {altura:.2f}m de altura e pesa {peso}kg. Isso resulta em um IMC de {imc:.2f}')

resultado = '{nome} tem {altura:.2f}m de altura e pesa {peso}kg. Isso resulta em um IMC de {imc:.2f}'
print(resultado.format(nome=nome, altura=altura, peso=peso, imc=imc))
print(resultado[-10:-37:-1])