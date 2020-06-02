

from abc import ABC, abstractmethod
class phone(ABC):
    def total(self, amount):
        print("You new iPhone purchase comes out to: ",amount)
    @abstractmethod
    def payment(self, amount):
        pass
    
    class FinancedPayments(phone):
        def payment(self, amount):
            print('Or you can finance your new iPhone for 3 years for {} a month '.format(amount))

    obj = FinancedPayments()
    obj.total("$1200")
    obj.payment("$54")


