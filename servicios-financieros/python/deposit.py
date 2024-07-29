from account_transaction import AccountTransaction

class Deposit(AccountTransaction):

    'instance creation'

    @classmethod
    def for_value(cls, a_value):
        return cls(a_value)

    'initialization'

    def __init__(self, a_value):
        self._value = a_value

    'value'

    def value(self):
        return self._value