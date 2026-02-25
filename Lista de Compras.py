import time
import platform
import os

def limpar_console():
        sistema = platform.system()
        if sistema == "Windows":
            os.system("cls")   # Comando para Windows
        else:
            os.system("clear") # Comando para Linux/Mac

def executar():
    lista_de_compras = []
    
    def lista():
        print('-=-=-=- Lista de Compras -=-=-=-')
        print(' -> Selecione a Opção Abaixo: ')
        print(' [1] Inserir Item')
        print(' [2] Apagar Item')
        print(' [3] Listar')
        print(' [4] Sair')
        resposta = input(' Resposta: ')
        limpar_console()
        
        if resposta == '1':
            item = input(' Item: ')
            lista_de_compras.append(item)

            print(' -> CARREGANDO...')
            time.sleep(1.5)
            print(' Item Adicionado!')
            time.sleep(1)
            limpar_console()
            return lista()
            
        
        if resposta == '2':
            apagar = input(' Informe o Índice do Produto: ')
            apagar = int(apagar)
            lista_de_compras.pop(apagar)

            print(' -> CARREGANDO...')
            time.sleep(1.5)
            print(' Item Apagado!')
            time.sleep(1)
            limpar_console()
            return lista()
            

        if resposta == '3':
            if len(lista_de_compras) == 0:
                print(' Nada Para Listar!')
                time.sleep(1)
                return lista()

            for indice, item in enumerate(lista_de_compras):
                print(indice, '-', item)

            time.sleep(5)
            print('-=-' * 15)
            print(' Voltar Para lista: ')
            print(' [1] Sim')
            reposta_menu = input(' Resposta: ')

            print('-=-' * 15)
            print(' -> CARREGANDO...')
            time.sleep(1.5)
            limpar_console()
            return lista()
        
        if resposta == '4':
            print(' -> CARREGANDO...')
            time.sleep(1.5)
            limpar_console()

        if resposta not in ['1', '2', '3', '4']:
            print(' Opção Inválida!')
            time.sleep(1.5)
            limpar_console()
            return lista()
    
    lista()


if __name__ == '__main__':
    executar()