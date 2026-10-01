class Bank_Account:

    bank_name = "State Bank of India"
    total_accounts = 0
    interest_rate = 4.0
    MIN_BALANCE = 500
    _next_account_number = 1001

    def __init__(self,holder_name,account_type,initial_deposit,pin):
        self.holder_name = holder_name
        self._account_number = Bank_Account._next_account_number

        if(account_type in ["Savings","Current"]):
            self._account_type = account_type
        else:
            raise ValueError("Entered an Invalid Account Type")

        if(initial_deposit >= 500):
           self.__balance = initial_deposit
        else:
            raise ValueError("Deposit minumun 500 or above")
            
        if(len(str(pin))==4):
            self.__pin = pin
        else:
            raise ValueError("Enter only 4 digits pin")

        Bank_Account.total_accounts += 1
        Bank_Account._next_account_number += 1


    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self.__balance

    def deposit(self,amount):
        if(amount<0):
            raise ValueError("Enter an Valid Amount")
        else:
            self.__balance += amount
            print("\namount deposited : check Balance\n")

    
    
    def __verify_pin(self,check):
           if(self.__pin != check):
               raise ValueError("Entered INcorrect pin Try again")
           else:
               return True

    def change_pin(self,old_pin,new_pin):
        if(self.__pin!=old_pin or len(str(new_pin))!=4):
            raise ValueError("Entered correct old pin / check that pin contains 4 digits only ")
        else :
               self.__pin = new_pin
               print(f"new pin updated sucessfuly\n")

    def add_annual_interest(self):
        return (self.__balace * Bank_Account.interest_rate ) / 100

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts
    
    @staticmethod
    def is_valid_amount(amount):
        if(amount >= 0):
            return True
        else:
            return False

    def __str__(self):
         return (f"Account Number: {self.account_number}\n"
                f"Holder Name    : {self.holder_name}\n"
                f"Account Type   : {self._account_type}\n"
                f"Balance        : {self.balance}")

    
    def withdraw(self,amount,pin):

        if(amount > 0 and self.__verify_pin(pin)  and (self.__balance - amount) >= Bank_Account.MIN_BALANCE):
            self.__balance -= amount
            print(f"\nMoney withdrawn sucessufly : {amount}\n")
        else :
            raise ValueError("unsufficient funds : check balance")



a1 = Bank_Account("Harsha","Current",4000,1185)

print(Bank_Account.get_total_accounts())

print(a1.__str__())
a1.change_pin(1185,9494)
a1.withdraw(2004,9494)
print(a1.__str__())
a1.deposit(87521)
print(a1.__str__())
print(a1.balance)
print(a1.is_valid_amount(-200))