import datetime
from random import randint
import time

print("----SENIOR'S BANK----")

class Accounts():
    def init(self, name, id):
        self.name = name
        self.id = id
        self.dic_account = {}
        print(self.dic_account)

    def add_info(self, key, value):
         self.key = key
         self.value = value
         self.dic_account[self.key] = self.value

    def open_ac():
        rn_name = input('Name:')
        rn_numb = randint(1000, 9999)
        rn_id = rn_name[0] + str(rn_numb)
        Accounts.add_info(rn_name, rn_id)

print("WELCOME TO SENIOR'S BANK")

login = input("Do you already have an account?[Y/N]").upper().strip()[0]

if login == "Y":
    name = input("What's your name?: ")
    id = input(str("What's your id?: "))
    Accounts(name, id)
elif login == "N":
    Accounts.open_ac()


