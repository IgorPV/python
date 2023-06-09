try:
    horario_str = input('Digite o horario(hh:mm): ')
    horario = int(horario_str.split(':')[0])
    if horario>=0 and horario<=11:
        print('Bom dia')
    elif horario>=12 and horario<=18:
        print('Boa tarde')
    else:
        print('Boa noite')
except:
    print('Nao foi inserido um horario')