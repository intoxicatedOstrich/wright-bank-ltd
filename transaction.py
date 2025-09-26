# transaction.py
from datetime import datetime

class Transaction:
    def __init__(self, amount, description, transaction_type = 'expense', date=None):
        if amount < 0:
            raise ValueError("Amount must be positive. Use transaction type to specify")
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description
        self.date = date if date else datetime.now()

    @property
    def net_amount(self):
        return self.amount if self.transaction ==  'income' else -self.amount


    def __str__(self):
        symbol = "+" if self.transaction_type == 'income' else "-"
        return f"{self.date.strftime('%Y-%m-%d')}: {symbol}${self.amount:.2f} - {self.description}"
