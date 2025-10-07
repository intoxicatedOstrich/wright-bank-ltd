from collections import *
import unittest

class Customer:
  # initialize id as a class var
  user_id = 1
  def __init__(self, name):
    # set it customer id to current id
    self.id = Customer.user_id
    self.name = name
    # Create a list to keep track of customer's accounts
    self.accounts = []
    # increment class var so next customer has a new id
    Customer.user_id += 1

  
  # define helper method to get info for debugging purposes
  def print_name_and_id(self):
    print("User:", self.name)
    print("Client ID: ", self.id)
  
  def add_bank_account(self, amount):
    new_account = BankAccount(amount)
    self.accounts.append(new_account)
    return new_account
  
  def print_accounts_and_balances(self):
    print(f"\n===={self.name}'s Accounts Summary====")
    for account in self.accounts:
      print("Account #: ", account.number)
      print("Balance: ", account.balance)
      print('------------------------------')
  
class BankAccount:
  account_number = 3000123456789
  def __init__(self, initial_deposit):
    self.balance = initial_deposit
    self.number = BankAccount.account_number
    BankAccount.account_number += 1
  
  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
      if self.balance >= amount:
        self.balance -= amount
      else:
        raise InsufficientFundsError("Insufficient funds")

class InsufficientFundsError(Exception):
    pass

def process_transactions(*args, **kwargs):
  for transaction in args:
    try:
      account, transaction_type, amount = transaction
      if transaction_type == 'deposit':
        account.deposit(amount)
        print(f"{amount} deposited successfully into account #{account.number}")
      if transaction_type == 'withdrawal':
        if account.balance < amount:
          raise InsufficientFundsError(f"Insufficient funds for withdrawal of {amount} \nCurrent Balance: {account.balance}")
        account.withdraw(amount)
        print(f"Withdrawal of {amount} from account #{account.number} successful ")
    except Exception as e:
      print(e)

def customer_accounts_generator(customer):
  for account in customer.accounts:
    yield account

def generate_financial_report(*customers):
  financial_report = defaultdict(list)
  for customer in customers:
    print(f"REPORT FOR {customer.name}")
    accounts_generator = customer_accounts_generator(customer)
    num_of_accounts = 0
    total_balance = 0
    for account in accounts_generator:
      num_of_accounts += 1
      total_balance += account.balance
    print(num_of_accounts)
    print(total_balance)
    financial_report[customer.name] = [num_of_accounts, total_balance]
  return financial_report

def print_financial_report(financial_report):
  for item in financial_report.items():
    print(item)

class TestCustomer(unittest.TestCase):
  def test_new_customer(self):
    new_customer_1 = Customer("test_1")
    self.assertEqual(new_customer_1.name, "test_1")
  
  def test_different_customers_same_name(self):
    new_customer_1 = Customer("test_1")
    new_customer_2 = Customer("test_1")
    self.assertEqual(new_customer_1.name, new_customer_2.name)
    self.assertNotEqual(new_customer_1.id,  new_customer_2.id)

  def test_new_customer_add_account(self):
    customer_1 = Customer("test")
    customer_1_acct_1 = customer_1.add_bank_account(1000)
    customer_1_acct_2 = customer_1.add_bank_account(10000)
    self.assertEqual(customer_1.accounts[0].balance, 1000)
    self.assertEqual(customer_1.accounts[1].balance, 10000)

class TestBankAccount(unittest.TestCase):
  def test_create_account(self):
    new_account = BankAccount(1000)
    self.assertEqual(new_account.balance, 1000)

  def test_deposit(self):
    new_account = BankAccount(1000)
    new_account.deposit(1000)
    self.assertEqual(new_account.balance, 2000)

  def test_withdrawal(self):
    new_account = BankAccount(1000)
    new_account.withdraw(500)
    self.assertEqual(new_account.balance, 500)
    
    with self.assertRaises(InsufficientFundsError):
      new_account.withdraw(550)  

class TestProcessTransactions(unittest.TestCase):
  def setUp(self):
    self.original_account_number = BankAccount.account_number

  def tearDown(self):
    BankAccount.account_number = self.original_account_number

  def test_process_transactions_updates_balances(self):
    account_1 = BankAccount(100)
    account_2 = BankAccount(200)

    process_transactions(
      (account_1, 'deposit', 50),
      (account_2, 'withdrawal', 150),
    )

    self.assertEqual(account_1.balance, 150)
    self.assertEqual(account_2.balance, 50)

  def test_process_transactions_continues_after_error(self):
    account_1 = BankAccount(100)
    account_2 = BankAccount(200)

    process_transactions(
      (account_1, 'withdrawal', 150),
      (account_2, 'deposit', 25),
    )

    self.assertEqual(account_1.balance, 100)
    self.assertEqual(account_2.balance, 225)

# unittest.main()

if __name__ == "__main__":
  aug = Customer('Aug')
  aug.print_name_and_id()
  aug_account_1 = aug.add_bank_account(100)
  aug_account_2 = aug.add_bank_account(20)
  aug_account_3 = aug.add_bank_account(38498)
  aug.print_accounts_and_balances()

  deb = Customer('Deb')
  deb_account_1 = deb.add_bank_account(10000)
  deb_account_2 = deb.add_bank_account(43769)

  process_transactions((aug_account_1, 'deposit', 2000), (aug_account_2, 'withdrawal', 40), (deb_account_1, 'withdrawal', 4768), (deb_account_2, 'deposit', 208000))
  aug.print_accounts_and_balances()
  deb.print_accounts_and_balances()
