# transaction.py
from datetime import datetime

class Transaction:
    def __init__(self, amount, description, date=None):
        self.amount = amount
        self.description = description
        self.date = date if date else datetime.now()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-$d')}: ${self.amount:.2f} - {self.description}"
