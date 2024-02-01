from random import randint

print("----SENIOR'S BANK----")

class Accounts:
    def init(self, name, id):
        self.name = name
        self.id = id
        self.dic_account = {}

    def add_info(self, key, value):
        self.dic_account[key] = value

def open_ac():
    rn_name = input("Name: ")
    rn_numb = randint(1000, 9999)
    rn_id = rn_name[0] + str(rn_numb)
    print(rn_id)
    return Accounts(rn_name, rn_id)  # Create and return an account object

print("WELCOME TO SENIOR'S BANK")

login = input("Do you already have an account?[Y/N]").upper().strip()[0]

if login == "Y":
    name = input("What's your name?: ")
    id = input("What's your id?: ")
    account = Accounts(name, id)  # Create account object
    # Add relevant information to the account
elif login == "N":
    account = open_ac()  # Call the function to create an account