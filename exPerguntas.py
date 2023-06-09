perguntas = [
    {
        'pergunta': 'quanto é 2+2?',
        'opções': ['1','2','3','4'],
        'resp': '4'
    },
    {
        'pergunta': 'qual o maior clube do mundo?',
        'opções': ['SPFC', 'Real Madrid', 'Manchester United'],
        'resp':'SPFC'
    }
]

def perguntados(perguntas):
    corretas = 0
    for pergunta in perguntas:
        texto = pergunta.get('pergunta')
        print(f'Responda, {texto}\n\n')
        print("Opções:")
        for pos, option in enumerate(pergunta['opções']):
            print(f'{pos} {option}')
        try:
            resposta = int(input('Qual a resposta? '))
            resposta_check = pergunta['opções'][resposta]
            if resposta_check == pergunta['resp']:
                corretas += 1
                print('Correta resposta')
            else:
                print('Resposta errada')
        except:
            print('Resposta errada!')
            continue
    else:
        print(f'Acertou {corretas} de {len(perguntas)}')


perguntados(perguntas)