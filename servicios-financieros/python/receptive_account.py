class ReceptiveAccount():

    'initialization'

    def __init__(self):
        self._transactions = []

    'balance'

    def balance(self):
        return sum([transaction.value() for transaction in self._transactions], 0)

    'transactions'

    def register(self, a_transaction):
        self._transactions.append(a_transaction)

    def transactions(self):
        return self._transactions.copy()

    'testing'

    def has_registered(self, a_transaction):
        return (a_transaction in self._transactions)