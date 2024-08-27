from random import randint
from time import sleep
import cpf_verificator

class Contas:
    def __init__(self):
        self.dic_conta = {"israel aureliano silva": "49454328808"}

    def verificar_conta(self, nome, cpf):
        print(self.dic_conta)
        if nome in self.dic_conta:
            if cpf in self.dic_conta.values():
                sleep(1.5)
                Menu_principal(nome).tela_1()
        else:
            print("Ocorreu um problema ao acessar sua conta, tente novamente ou crie uma conta!")
    
    def abrir_conta(self):
        nome = input('Digite seu nome para abrir a conta: ')
        cpf_user = str(input("Digite seu CPF: "))
        self.verificar_cpf_abrir_conta(nome, cpf_user)

    def verificar_cpf_verificar_conta(self, nome, cpf):
        self.resultado = cpf_verificator.Verificador().verificar(cpf)
        if self.resultado:
            self.verificar_conta(nome, cpf)
        else:
            print("CPF inválido")
    
    def verificar_cpf_abrir_conta(self, nome, cpf):
        self.resultado = cpf_verificator.Verificador().verificar(cpf)
        if self.resultado:
            if cpf not in self.dic_conta.values():
                self.dic_conta[nome] = cpf
                self.verificar_conta(nome, cpf)
            else:
                print("Esse CPF já está cadastrado em uma outra conta! Tente outra vez")
                self.abrir_conta()
        else:
            print("CPF inválido, tente novamente")
            self.abrir_conta()


class Menu_principal:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 1000

    def tela_1(self):
        print(f"Bem-vindo, {self.nome}! Seu saldo é de {self.saldo}R$")
        
        while True:
            decisao = str(input("Você deseja depositar um valor?[depositar]\nVocê deseja fazer um pix?[pix]\nVocê deseja sacar um valor?[sacar] ")).lower()
        
            if decisao == "sacar":
                self.sacar()
            elif decisao == "depositar":
                self.depositar()
            elif decisao == "pix":
                self.pix()
            else:
                print("Algo deu errado, tente novamente!")

    def sacar(self):
        while True:
            valor = int(input(f"quanto você deseja sacar? seu saldo é de {self.saldo}"))
            if valor > 0:
                if valor <= self.saldo:
                    self.saldo -= valor
                    print(f"seu saldo agora é de {self.saldo}R$")
                    sleep(1.5)
                    decisao_2 = str(input("deseja sacar mais algum valor? [S/N]")).lower()
                    if decisao_2 == "s":
                        continue
                    elif decisao_2 == "n":
                        print("voltando ao menu principal")
                        self.tela_1()
                        break
                    else:
                        print("algo deu errado")
                elif valor >= self.saldo:
                    decisao_2 = str(input("saldo insuficiente! deseja sacar outro valor?[S/N]")).lower()
                    if decisao_2 == "s":
                        continue
                    elif decisao_2 == "n":
                        print("voltando ao menu principal")
                        self.tela_1()
                        break
                    else:
                         print("algo deu errado")
                else:
                    print("erro na transação, voltando ao menu inicial...")
                    self.tela_1()
            else:
                decisao_2 = input("algo deu errado, deseja tentar novamente?[S/N]").lower()
                if decisao_2 == "s":
                    self.sacar()
                else:
                    print("voltando ao menu principal...")
                    sleep(1.5)
                    self.tela_1()

    def depositar(self):
        print("Depósito realizado com sucesso")

    def pix(self):
        print("Pix realizado com sucesso")
    

print("BEM-VINDO AO BANCO HORIZON TRUST")
sleep(1.5)

login = input("Você já possui uma conta?[S/N]").upper().strip()[0]

if login == "S":
    nome = input("Qual é o seu nome?: ")
    cpf = str(input("Qual é o seu CPF?: "))
    Contas().verificar_cpf_verificar_conta(nome, cpf)

elif login == "N":
    Contas().abrir_conta()
