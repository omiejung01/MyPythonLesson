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
        self.__extended_until_date = None
        super().__init__(account_name, opening_balance)

    def display(self):
        # Method override
        # Polymorphism #1
        return super().display() + ' credit: ' + f"{self.__credit:,.2f}"


def my_sum(args):
    # input can be string, list of int, or dictionary of int
    # Polymorphism #2 (data type)
    sum = 0
    if type(args) == str:
        numbers = args.split()
        for n in numbers:
            sum += int(n)

    if type(args) == list:
        for n in args:
            sum += n

    if type(args) == dict:
        vals = args.values()
        for n in vals:
            sum += n

    return sum

def display_name(firstname, lastname = '', title = ''):
    # this method can have one, two and three arguments !!
    # Polymorphism #3 (default argument)
    if title == '':
        title = 'Khun'

    if lastname == '':
        return title + ' ' + firstname + '\n'
    else:
        return title + ' ' + firstname + ' ' + lastname + '\n'

def q01():
    MyAccount1 = Account('Client #1', 5000)
    print(MyAccount1.display())

    MyAccount2 = CreditCard(20000, 'Client #2', 5000)
    print(MyAccount2.display())
def q02():
    print(my_sum('10 20 30'))
    print(my_sum([10, 20, 31]))
    num = {
        '#1': 10,
        '#2': 20,
        '#3': 32
    }
    print(my_sum(num))

def q03():
    print(display_name('Albedo'))
    print(display_name('Eula', 'Lawrence'))
    print(display_name('Prinzessin', 'der Verurteilung!','mein Fräuleins'))

def run():
    """
    q01()
    q02()
    """
    q03()

