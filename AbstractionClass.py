

from abc import ABC, abstractmethod
class phone(ABC):
    @abstractmethod
    def total(self, amount):
        print('You new iPhone purchase comes out to: {}'.format(amount))
    def payment(amount):
        pass

class FinancedPayments(ABC):
    @staticmethod
    def payment(amount):
        print('Or you can finance your new iPhone for 3 years for {} a month '.format(amount))
    def total(self, amount):
        print('Giving you a grand total of... {}'.format(amount))

obj = FinancedPayments()
obj.total("$1200")
obj.payment("$54")


