from abc import ABC, abstractmethod
from billing_account.billing_account import BillingAccount
from payee.payee import Payee

class PaymentStrategy(ABC):

    @abstractmethod
    def process_payment(self, account: BillingAccount, payee: Payee, amount: float) -> str:
        pass