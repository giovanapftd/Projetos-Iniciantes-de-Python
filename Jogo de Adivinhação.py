
import random

print('-=-=-=- Jogo de Adivinhação -=-=-=-')
print('-=-=-=-=-  Seja Bem Vindo -=-=-=-=-')
print(' ')
max =input(' Digite até que número eu posso escolher: ')
print(' ')

if max.isdigit():
    max = int(max)
else:
    print(' Erro: Valor Informado Não É Numérico!')
    quit()

resposta_computador = random.randint(0, max + 1)
n_escolha = 0
print('-=-' * 12)

while True:
    resposta_usuario = input(' Adivinhe o número: ')

    if resposta_usuario.isdigit():
        resposta_usuario = int(resposta_usuario)

    else:
        print(' Erro: Valor Informado Não É Numérico!')
        continue

    n_escolha = n_escolha + 1

    if resposta_usuario == resposta_computador:
        print(' PARABÉNS, VOCÊ ACERTOU!')
        break
                
    elif resposta_usuario > resposta_computador:
        print(' ')
        print('Chutou alto, o número é menor que isso...') 
    else:
        print(' ')
        print('Chutou baixo, o número é maior que isso...')
print('Nº de tentativas: ' + str(n_escolha))
