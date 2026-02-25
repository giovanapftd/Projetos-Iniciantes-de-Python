import time
import sys
import os
import platform

def dolar(x):
    return(x / 5.37)

def euro(x):
    return(x / 6.25)

def libra(x):
    return(x / 7.21)



def limpar_console():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")   # Comando para Windows
    else:
        os.system("clear") # Comando para Linux/Mac



def novamente():
    print('-=-' * 27)
    print(' Você deseja usar novamente?')
    print(' [1] Sim')
    print(' [2] Não')
    print('-=-' * 27)

    resposta = input(' Resposta: ')
    if resposta == '1':
        limpar_console()
        executar()
    else:
        limpar_console()
        print(' OBRIGADA POR USAR NOSSO CONVERSOR DE MOEDAS!')
        time.sleep(5)

def menu():
    print('-=-=-=- CONVERSOR DE MOEDAS -=-=-=-')
    print(' PARA QUAL MOEDA SERÁ CONVERTIDO O VALOR')
    print(' [1] DÓLAR')
    print(' [2] EURO')
    print(' [3] LIBRA')
    print('-=-' * 12)



def escolha():
    resposta_usuario = input(' Resposta [1/2/3]: ')

    print('-=-' * 12)
    time.sleep(1)

    if resposta_usuario not in '123':
        print(' -> OPÇÃO INVÁLIDA!')
        print(' ')
        sys.stdout.write("\033[F")  
        sys.stdout.write("\033[K")
        sys.stdout.flush()
        print('-=-' * 12)
        return escolha()
    
    try:
        valor1 = int(input(' Digite o valor que será convertido: '))
        time.sleep(1)
        print('-=-' * 12)

    except:
        print(" -> OPÇÃO INVÁLIDA!")
        print(' ')
        sys.stdout.write("\033[F")  
        sys.stdout.write("\033[K")
        sys.stdout.flush()
        print('-=-' * 12)
        return escolha()
    
    if resposta_usuario == '1':
        print(f' R$: {valor1}')
        time.sleep(1)
        print(f' USD: {dolar(valor1):.2f}')

    if resposta_usuario == '2':
        print(f' R$: {valor1}')
        time.sleep(1)
        print(f' EUR: {euro(valor1):.2f}')

    if resposta_usuario == '3':
        print(f' R$: {valor1}')
        time.sleep(1)
        print(f' GBP: {euro(valor1):.2f}')

    novamente()



def executar():
    menu()
    escolha()

if __name__ == '__main__':
    executar()