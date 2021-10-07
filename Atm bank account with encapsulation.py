class bankAccount():
    '''This is a bank account class'''
    def __init__(self, account_name = 'Current Acount', balance = 100000):
        self.__account_name = account_name
        self.__balance = balance

    def balanceGetter(self):
        print (self.__balance)


    def balanceSetter_withdraw(self, value):
        if value < self.__balance:
            self.__balance = self.__balance - value
            print ("New balance :", self.__balance)
        else:
            print ("You dont have enough funds!")

accountObject = bankAccount()

while True:
     print ("1. Check Account Balance")
     print ("2. Withdraw funds")
     menu_option = int(input())
     if menu_option == 1:
            accountObject.balanceGetter()
     elif menu_option == 2:
            value = int(input("How much u want to Withdraw?"))
            accountObject.balanceSetter_withdraw(value)
     else:
            print ("wrong menu choice")
input()            
