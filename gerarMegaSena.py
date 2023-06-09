import random

num = int(input('numero de dezenas [6 a 10]'))
lista_ini = []

for i in range(0,num):
    lista_ini.append(random.randint(1,60))

lista_corrigida = list(set(lista_ini))
if len(lista_corrigida) < num:
    lista_corrigida.append(random.randint(1,60))

print(sorted(lista_corrigida))
