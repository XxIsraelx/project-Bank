from random import randint
from time import sleep
import cpf_verificator

class Contas():
    def __init__(self):
        self.dic_conta = {"israel aureliano silva" : "49454328808"}

    def verificar_conta(self, nome, cpf):
        print(self.dic_conta)
        if nome in self.dic_conta:
            if cpf in self.dic_conta.values():
                print(f"bem vindo! {nome}")
        else:
            print("Ocorreu um problema ao acessar sua conta, tente novamente ou crie uma conta!")
    
    def abrir_conta(self):
        nome = input('Digite seu nome para abrir a conta :')
        cpf_user = str(input("Digite seu CPF : "))
        self.verificar_cpf_abrir_conta(nome, cpf_user)

    def verificar_cpf_verificar_conta(self, nome, cpf):
        self.resultado = cpf_verificator.Verificador().verificar(cpf)
        if self.resultado:
            self.verificar_conta(nome, cpf)
        else:
            print("cpf invalido")
    
    def verificar_cpf_abrir_conta(self, nome, cpf):
        self.resultado = cpf_verificator.Verificador().verificar(cpf)
        if self.resultado:
            if cpf not in self.dic_conta.values():
                self.dic_conta[nome] = cpf
                self.verificar_conta(nome, cpf)
            else:
                print("Esse CPF ja está cadastrado em uma outra conta!, tente outra vez")
                self.abrir_conta()


        else:
            print("cpf invalido, tente novamente")
            self.abrir_conta()

print("BEM-VINDO AO BANCO HORIZON TRUST")
sleep(1.5)

login = input("Você já possui uma conta?[S/N]").upper().strip()[0]

if login == "S":
    nome = input("Qual é o seu nome?: ")
    cpf = str(input("Qual é o seu cpf?: "))
    Contas().verificar_cpf_verificar_conta(nome, cpf)

elif login == "N":
    conta = Contas().abrir_conta()
    
        

