import time
class Conta():

    def __init__(self, nome,):
        self.nome = nome
        print(f'Bem vindo {nome}')
    
    def adcionar(adcionar):
        poupança = 100
        valor = adcionar
        total = poupança+valor
        print(f'O total da sua conta é de {total}')

    def retirar(retirar):
        poupança = 100
        valor = retirar
        if poupança > valor:
            total = poupança-valor
            print(f'\nO total da sua conta é de {total}')
        else:
            print(f'Nao é possivel retirar {valor}, pois seu saldo é de {poupança}')





p1 = input('olá, qual seu nome? ')
time.sleep(0.5)
Entrar = Conta(p1)
print(f"Esse é o menu de transaçoes!")
time.sleep(0.5)

deciçao = input("\nEscolha [A] para adcionar um valor " "\nEscolha {B} para tirar um valor ")
time.sleep(0.5)
if deciçao == "a":
    valor1 = int(input('Digite um valor '))
    time.sleep(0.5)
    menu1 = Conta.adcionar(valor1)
elif deciçao == 'b':
    valor2 = int(input('Digite um valor '))
    time.sleep(0.5)
    menu2 = Conta.retirar(valor2)
    




     




