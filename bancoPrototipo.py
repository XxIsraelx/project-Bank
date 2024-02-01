import time
class Conta():

    def __init__(self, nome,):
        self.nome = nome
        print(f'Bem vindo {nome}')

    def menuTransaçoes():
        time.sleep(1.5)
        print(f"\nEsse é o menu de transaçoes!")
        time.sleep(0.5)
        deciçao = input("\nEscolha [A] para depositar um valor " "\nEscolha [B] para sacar um valor ")
        time.sleep(0.5)
        if deciçao == "a":
            valor1 = int(input('Digite um valor '))
            time.sleep(0.5)
            menu1 = Conta.depositar(valor1)
        elif deciçao == 'b':
            valor2 = int(input('Digite um valor '))
            time.sleep(0.5)
            menu2 = Conta.sacar(valor2)
    
    def depositar(adcionar):
        poupança = 0
        valor = adcionar
        poupança += valor
        print(f'O total da sua conta é de {poupança}')
        time.sleep(1.5)
        _escolha = input(f'deseja continuar no menu de transaçoes? [S] ou [N]')
        if _escolha == 'S' or 's':
            time.sleep(1.5)
            Conta.menuTransaçoes()
        elif _escolha == 'n' or 'N':
            print('o banco agradece sua visita!')
            exit()
           
            
       
    def sacar(retirar):
        poupança = 100
        valor = retirar
        if poupança > valor:
            poupança -= valor
            print(f'\nO total da sua conta é de {poupança}')
        else:
            print(f'Nao é possivel retirar {valor}, pois seu saldo é de {poupança}')





p1 = input('olá, qual seu nome? ')
time.sleep(0.5)
entrar = Conta(p1)

escolha = str(input("\nVoce deseja acessar o menu de transaçoes? [S] ou [N]"))
if escolha == "s" or "S":
    print('aguarde...')
    Conta.menuTransaçoes()
else:
    exit()
    

    




     




