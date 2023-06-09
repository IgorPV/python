nome = input('Digite seu primeiro nome: ')
nome_certo = nome.strip()
if len(nome_certo) <=4:
    print('Seu nome é curto')
elif len(nome_certo) > 4 and len(nome_certo) <= 6:
    print('Seu nome é de tamanho regular')
else:
    print('Seu nome é muito grande')