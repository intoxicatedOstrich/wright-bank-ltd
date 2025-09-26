# test_basic.py

# import the Transaction class from Transation.py
from transaction import Transaction
from datetime import datetime

t1 = Transaction(50.00, "Groceries")
t2 = Transaction(1500.00, "Salary", transaction_type = 'income')
t3 = Transaction(30.00, "Coffee Shop")

print("Testing Transaction Creation:")
print()
print(t1)
print(t2)
print(t3)

print(f"\n Transaction amount: {t1.amount}")
print(f"\n Transaction description: {t1.description}")
print(f"\n Transaction date: {t1.date}")
