class AccountTransaction():

    'instance creation'

    @classmethod
    def register_on(cls, a_value, an_account):
        transaction = cls.for_value(a_value)

        an_account.register(transaction)

        return transaction

    'value'

    def value(self):
        raise NotImplementedError("Should be implemented by the subclass")