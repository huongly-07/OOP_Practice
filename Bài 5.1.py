class Money:
    def __init__(self, amount=0, currency='VND'):
        self.amount=int(amount)
        self.currency=str(currency)
    def __str__ (self):
        return(f'{self.amount} {self.currency}')
    def __eq__(self, other):
        if isinstance(other,Money):
            return self.amount==other.amount and self.currency==other.currency
        return False