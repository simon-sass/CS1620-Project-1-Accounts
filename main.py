from accounts import *


def main():
    a1 = Account('John')
    print(a1)                   # Account name = John, Account balance = 0.00
    a1.deposit(-20.50)
    a1.deposit(0)
    a1.deposit(50)
    a1.withdraw(10.5)
    print(a1)                   # Account name = John, Account balance = 39.50

    a2 = SavingAccount('Jane')
    print(a2)                   # SAVING ACCOUNT: Account name = Jane, Account balance = 100.00
    a2.deposit(-20.50)
    a2.deposit(0)
    a2.deposit(50)
    a2.withdraw(10)
    print(a2)                   # SAVING ACCOUNT: Account name = Jane, Account balance = 140.00
    a2.deposit(50)
    a2.deposit(10.5)
    a2.deposit(5)
    a2.deposit(100)
    print(a2)                   # SAVING ACCOUNT: Account name = Jane, Account balance = 311.61
    a2.withdraw(212)
    print(a2)                   # SAVING ACCOUNT: Account name = Jane, Account balance = 311.61
    a2.withdraw(211.61)
    print(a2)                   # SAVING ACCOUNT: Account name = Jane, Account balance = 100.00


if __name__ == '__main__':
    main()
    