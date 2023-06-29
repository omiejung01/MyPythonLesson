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

def sum1(num):
   sum = 0
   # [1, 2 , 3, 4, 5]
   for x in range(1, num+1):
       sum += x
   return sum


def sum2(num):
   if num == 0:
       return 0
   elif num == 1:
       return 1
   else:
       return num + sum2(num - 1)
   # 5 + 4 + 3 + 2 + 1


def factorial(num):
   if num == 0:
       return 1
   elif num == 1:
       return 1
   else:
       return num * factorial(num - 1)
   # 5 * 4 * 3 * 2 * 1


def run():
   #print(sum2(10))
   print(factorial(7))


   score1 = 87
   score2 = 45
   score3 = 61
   average = (score1+score2+score3)/3


   mylist = [3, 7, 6, 9, 8, 3]


   mylist2 = []
   mylist2.append(3)
   mylist2.append(7)
   mylist2.append(6)


   C = 'c'
   mylist3 = ['A','B', C ]
   #String


   mystring = 'This is a book'


   print('Number of chars is ', len(mystring))
   print(len(mylist3))