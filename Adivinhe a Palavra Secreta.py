import random
import time
import platform
import os

def limpar_console():
        sistema = platform.system()
        if sistema == "Windows":
            os.system("cls")   # Comando para Windows
        else:
            os.system("clear") # Comando para Linux/Mac

def novamente():
        print(' Você deseja usar novamente?')
        print(' [1] Sim')
        print(' [2] Não')
        print('-=' * 23)

        resposta = input(' Resposta: ')
        if resposta == '1':
            limpar_console()
            executar()
        else:
            limpar_console()
            print(' OBRIGADA POR JOGAR!')
            time.sleep(3)



def executar():
    
    def palavra_secreta(caminho='palavras.txt'):
        from pathlib import Path
        p = Path(caminho)

        try:
            with p.open(encoding='utf-8') as f:
                palavras = [s for linha in f if (s := linha.strip())]
                resposta = random.choice(palavras).lower()
                qtd_caracteres = len(resposta)

        except FileNotFoundError:
            print(f'Arquivo {caminho} não encontrado!')
            return None
    
        def jogo():
            print('-=-=-= ADIVINHE A PALAVRA SECRETA =-=-=-=')
            print(f' A Palavra Possui {qtd_caracteres} Letras -> "{'*' * qtd_caracteres}"')
            print('-=' * 21)

            letras_acertadas = ''
            tentativas = 0
            while True:
                letra = input(' Digite Uma Letra: ').strip()
                tentativas += 1

                if len(letra) != 1:
                    print('-> DIGITE SOMENTE UMA LETRA!')
                    print('-=' * 21)
                    time.sleep(1.5)
                    limpar_console()
                    return jogo()

                elif not letra.isalpha():
                    print('-> DIGITE SOMENTE LETRAS!')
                    print('-=' * 21)
                    time.sleep(1.5)
                    limpar_console()
                    return jogo()
                
                if letra in resposta:
                    letras_acertadas += letra 

                palavra_formada = ''
                for letra_secreta in resposta:
                    if letra_secreta in letras_acertadas:
                        palavra_formada += letra_secreta

                    else:
                        palavra_formada += '*'
                print(palavra_formada)
                time.sleep(1)

                if palavra_formada == resposta:
                    limpar_console()
                    print('PARABÉNS, VOCÊ GANHOU!')
                    print(f'A PALAVRA SECRETA ERA: {palavra_formada}')
                    print(f'TENTATIVAS: {tentativas}')
                    print('-=' * 21)
                    time.sleep(2)
                    break
                
            novamente()


        jogo()
    palavra_secreta()

if __name__ == '__main__':
    executar()