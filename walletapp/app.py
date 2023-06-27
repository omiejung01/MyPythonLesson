message2 = 'Sawasdee'

class Account:
    def __init__(self,account_name,opening_balance):
        self.account_name = account_name
        self.balance = opening_balance
    def display(self):
        #Balance Inquiry
        return self.account_name + ' ' + f"{self.balance:,.2f}"
    def setAccountName(self, new_name):
        self.account_name = new_name


def hello2():
    message = 'Hello2'
    print(message)
def hello():
    print('Hello World')
    s = 1
    print(message2)

    jane_account = Account('Jane',1200.00)

    print(jane_account.account_name)
    print(jane_account.display())

    jane_account.setAccountName('Jane2')
    print(jane_account.display())

    # print(message) # You cannot access other function's variable
