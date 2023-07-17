from datetime import datetime
class Account():
    def __init__(self,account_name,opening_balance):
        self.__account_name = account_name
        self.__balance = opening_balance
        self.__created_date = datetime.now()
        self.__activated = True

    def display(self):
        status = 'Deactivated'
        if self.__activated:
            status = 'Activated'
        return self.__account_name + ' - since ' + self.__created_date.strftime("%b %d, %Y") + ' - status: ' + status

    def balanceInquiry(self):
        # Balance Inquiry
        return f"{self.__balance:,.2f}"

class CreditCard(Account):
    def __init__(self, credit, account_name, opening_balance):
        self.__credit = credit
        self.__due_date = None
        self.__extended_limit = 0
        self.__extended_unitil_date = None
        super().__init__(account_name, opening_balance)

    def display(self):
        #Method override
        return super().display() + ' credit: ' + f"{self.__credit:,.2f}"


def run():
    MyAccount1 = Account('Client #1', 5000)
    print(MyAccount1.display())

    MyAccount2 = CreditCard(20000, 'Client #2', 5000)
    print(MyAccount2.display())

