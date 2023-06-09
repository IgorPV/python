lista_compras = []
while True:
    operacao = input('Informe o que deseja fazer, \n [i]nserir, [a]pagar, [l]istar: ').lower()
    try:
        if operacao == 'i':
            lista_compras.append(input('Entre com o item: '))
        elif operacao == 'a':
            lista_compras.pop(int(input('Insira o indice do item a ser removido: ')))
        elif operacao == '1':
            for ind, item in enumerate(lista_compras):
                print(ind, item)
        else:
            print('Valor inválido, tente novamente')
    except:
        print('Ocorreu um erro na operação selecionada, tente novamente')