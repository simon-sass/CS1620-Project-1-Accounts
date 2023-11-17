class Account:
    """
    A class representing a basic bank account.

    :ivar str name: The name associated with the account.
    :ivar float balance: The balance of the account.

    :param name: The name associated with the account.
    :type name: str
    :param balance: The initial balance of the account (default is 0).
    :type balance: float
    """

    def __init__(self, name: str, balance: float = 0):
        self.__account_name: str = name
        self.__account_balance: float = balance
        self.set_balance(balance)

    def deposit(self, amount: float) -> bool:
        """
        Deposits a specified amount into the account.

        :param float amount: The amount to deposit.
        :return: True if the deposit is successful, False otherwise.
        :rtype: bool
        """
        if amount <= 0:
            return False
        self.__account_balance += amount
        return True
    
    def withdraw(self, amount: float) -> bool:
        """
        Withdraws a specified amount from the account.

        :param float amount: The amount to withdraw.
        :return: True if the withdrawal is successful, False otherwise.
        :rtype: bool
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True
    
    def get_balance(self) -> float:
        """
        Returns the current balance of the account.

        :return: The current balance of the account.
        :rtype: float
        """
        return self.__account_balance
    
    def get_name(self) -> str:
        """
        Returns the name associated with the account.

        :return: The name associated with the account.
        :rtype: str
        """
        return self.__account_name
    
    def set_balance(self, value: float):
        """
        Sets the balance of the account to the specified value.

        :param float value: The value to set the balance to.
        """
        if value >= 0:
            self.__account_balance = value

    def set_name(self, value: str):
        """
        Sets the name associated with the account to the specified value.

        :param str value: The value to set the name to.
        """
        self.__account_name = value

    def __str__(self) -> str:
        """
        Returns a string representation of the account.

        :return: A string representation of the account.
        :rtype: str
        """
        return f"Account name = {self.get_name()}, Account balance = {self.get_balance():.2f}"

class SavingAccount(Account):
    """
    A class representing a savings account, inheriting from the Account class.

    :cvar float MINIMUM: The minimum balance required for a savings account.
    :cvar float RATE: The interest rate for the savings account.

    :param name: The name associated with the savings account.
    :type name: str
    """

    MINIMUM: float = 100
    RATE: float = 0.02

    def __init__(self, name: str):
        super().__init__(name, SavingAccount.MINIMUM)
        self.__deposit_count: int = 0
    
    def apply_interest(self):
        """
        Applies interest to the savings account balance based on the defined interest rate.
        """
        self.set_balance(self.get_balance() * (1 + SavingAccount.RATE))

    def deposit(self, amount: float) -> bool:
        """
        Deposits a specified amount into the savings account, applying interest if eligible.

        :param float amount: The amount to deposit.
        :return: True if the deposit is successful, False otherwise.
        :rtype: bool
        """
        if super().deposit(amount):
            self.__deposit_count += 1
            if self.__deposit_count % 5 == 0:
                self.apply_interest()
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        """
        Withdraws a specified amount from the savings account, considering the minimum balance.

        :param float amount: The amount to withdraw.
        :return: True if the withdrawal is successful, False otherwise.
        :rtype: bool
        """
        if amount <= 0 or amount > self.get_balance() - SavingAccount.MINIMUM:
            return False
        self.set_balance(self.get_balance() - amount)
        return True

    def set_balance(self, value: float):
        """
        Sets the balance of the savings account to the specified value, ensuring it meets the minimum requirement.

        :param float value: The value to set the balance to.
        """
        if value >= SavingAccount.MINIMUM:
            super().set_balance(value)

    def __str__(self) -> str:
        """
        Returns a string representation of the savings account.

        :return: A string representation of the savings account.
        :rtype: str
        """
        return f"SAVING ACCOUNT: {super().__str__()}"
