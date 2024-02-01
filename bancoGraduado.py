from random import randint

print("----BANCO DOS SENIORES----")

class Contas():
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.dic_conta = {}

    def add_info(self, chave, valor):
        self.dic_conta[chave] = valor

    def abrir_conta(self):
        nome = input('Nome:')
        numero_aleatorio = randint(1000, 9999)
        id_conta = nome[0] + str(numero_aleatorio)
        print(id_conta)
        return nome, id_conta

print("BEM-VINDO AO BANCO DOS SENIORES")

login = input("Você já possui uma conta?[S/N]").upper().strip()[0]

if login == "S":
    nome = input("Qual é o seu nome?: ")
    id = input("Qual é o seu id?: ")
    conta = Contas(nome, id)
elif login == "N":
    nome_conta, id_conta = Contas("","").abrir_conta()
    conta = Contas(nome_conta, id_conta)

chave_info_adicional = input("Digite a chave da informação adicional: ")
valor_info_adicional = input("Digite o valor da informação adicional: ")

conta.add_info(chave_info_adicional, valor_info_adicional)