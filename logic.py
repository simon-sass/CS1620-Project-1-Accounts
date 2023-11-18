from accounts import *
from gui import *
from PyQt6.QtWidgets import *
import csv

class Logic(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_1.clicked.connect(self.sign_in)
        self.button_2.clicked.connect(self.create_account)
        self.log_out_button.clicked.connect(self.log_out)
        self.add_interest_button.clicked.connect(self.add_interest)

    def create_account(self):
        csvfile = open('accounts_data.csv', 'r', newline='')
        reader = csv.reader(csvfile)
        username = self.lineEdit_1.text()
        password = self.lineEdit_2.text()
        account_type = self.savings_radio.isChecked() # True means the account is a savings account, false for a checking account
        if username in [line[0] for line in reader]: # List comprehension checking first value of every line in csv
            self.label_3.setText("\nUsername not available\nAlready in use")
        else:
            csvfile.close()
            csvfile = open('accounts_data.csv', 'a', newline='')
            writer = csv.writer(csvfile)
            starting_bal = 0
            if account_type:
                starting_bal += SavingAccount.MINIMUM
            writer.writerow([username, password, account_type, starting_bal])
            self.label_3.setText(f"\nNew account successfully created\nName : {username}\nStarting balance : {starting_bal}")
        csvfile.close()

    def sign_in(self):
        csvfile = open('accounts_data.csv', 'r', newline='')
        reader = csv.reader(csvfile)
        username = self.lineEdit_1.text()
        password = self.lineEdit_2.text()
        for line in reader:
            if username == line[0] and password == line[1]:
                if line[2] == "True":
                    self.current_account = SavingAccount(username, float(line[3]))
                else:
                    self.current_account = Account(username, float(line[3]))
                self.label_3.setText(f"\nSuccessfully signed into account {username}\nYour current balance is : {float(line[3]):.02f}")
                self.button_1.setText("Deposit")
                self.button_2.setText("Withdrawal")
                self.button_1.clicked.connect(self.deposit)
                self.button_2.clicked.connect(self.withdrawal)
                self.button_1.clicked.disconnect(self.sign_in)
                self.button_2.clicked.disconnect(self.create_account)
                if line[2] == "True":
                    self.add_interest_button.setEnabled(True)
                self.log_out_button.setEnabled(True)
                self.lineEdit_1.setEnabled(False)
                self.label_2.setText("Amount")
                self.lineEdit_2.setText("")
                csvfile.close()
                return
            elif username == line[0]:
                self.label_3.setText("\nPassword invalid")
                csvfile.close()
                return
        self.label_3.setText("\nAccount not found")
        csvfile.close()

    def log_out(self):
        self.current_account = None
        self.log_out_button.setEnabled(False)
        self.add_interest_button.setEnabled(False)
        self.lineEdit_1.setEnabled(True)
        self.button_1.clicked.connect(self.sign_in)
        self.button_2.clicked.connect(self.create_account)
        self.button_1.clicked.disconnect(self.deposit)
        self.button_2.clicked.disconnect(self.withdrawal)
        self.label_2.setText("Password")
        self.lineEdit_2.setText("")
        self.button_1.setText("Sign In")
        self.button_2.setText("Create Account")
        self.label_3.setText("Successfully signed out")

    def deposit(self):
        try:
            if not self.current_account.deposit(float(self.lineEdit_2.text())):
                self.label_3.setText(f"\nSuccessfully signed into account {self.current_account.get_name()}\nYour current balance is : {self.current_account.get_balance():.02f}\nEnter a positive valid amount (ex. 5.31)")
                return
        except:
            self.label_3.setText(f"\nSuccessfully signed into account {self.current_account.get_name()}\nYour current balance is : {self.current_account.get_balance():.02f}\nEnter valid amount (ex. 5.31)")
            return
        self.update_csv_line("accounts_data.csv", self.current_account.get_name(), self.current_account.get_balance())
        self.label_3.setText(f"\nSuccessfully signed into account {self.current_account.get_name()}\nYour current balance is : {self.current_account.get_balance():.02f}\nTransaction successful\nAdded {float(self.lineEdit_2.text()):.02f} to your account")

    def withdrawal(self):
        try:
            if not self.current_account.withdraw(float(self.lineEdit_2.text())):
                self.label_3.setText(f"\nSuccessfully signed into account {self.current_account.get_name()}\nYour current balance is : {self.current_account.get_balance():.02f}\nWithdrawing this amount would overdraft\nSelect a lower amount")
                return
        except:
            self.label_3.setText(f"\nSuccessfully signed into account {self.current_account.get_name()}\nYour current balance is : {self.current_account.get_balance():.02f}\nEnter valid amount (ex. 5.31)")
            return
        self.update_csv_line("accounts_data.csv", self.current_account.get_name(), self.current_account.get_balance())
        self.label_3.setText(f"\nSuccessfully signed into account {self.current_account.get_name()}\nYour current balance is : {self.current_account.get_balance():.02f}\nTransaction successful\nRemoved {float(self.lineEdit_2.text()):.02f} from your account")

    def add_interest(self):
        self.current_account.apply_interest()
        self.update_csv_line("accounts_data.csv", self.current_account.get_name(), self.current_account.get_balance())
        self.label_3.setText(f"\nSuccessfully signed into account {self.current_account.get_name()}\nYour current balance is : {self.current_account.get_balance():.02f}\nSuccessfully applied interest to your account")

    def update_csv_line(self, file_path, target_account, new_balance):
        lines = []
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == target_account:
                    row[3] = new_balance
                lines.append(row)

        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(lines)