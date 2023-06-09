import os

palavra_secreta = 'pigas'
palavra_tela = ''

for letra_sec in palavra_secreta:
    palavra_tela += '*'
tentativas = 1
while tentativas<=10:
    print(palavra_tela)

    if palavra_tela == palavra_secreta:
        os.system('cls')
        print(f'Parabéns, você acertou! A palavra era {palavra_secreta}')
        print(f'Você acertou em {tentativas-1} tentativas')
        break

    print(f'Tentativa {tentativas}')
    letra = input('Entre com uma letra ').lower()

    if letra in palavra_secreta:
        for num in range(len(palavra_secreta)):
            if palavra_secreta[num] == letra:
                palavra_tela = palavra_tela[:num] + letra + palavra_tela[num+1:]
    else:
        continue
    tentativas += 1
else:
    os.system("cls")
    print('Fim de Jogo.')