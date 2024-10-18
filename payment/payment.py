from patterns.strategy.payment_strategy import PaymentStrategy
from billing_account.billing_account import BillingAccount
from payee.payee import Payee

class Payment():
    def __init__(self, strategy: PaymentStrategy):

        if isinstance(strategy, PaymentStrategy):
            self.strategy = strategy
        else:
            raise ValueError("Invalid Strategy")
        
    def pay_bill(self, account: BillingAccount, payee: Payee, amount: float) -> str:
        return self.strategy.process_payment(account, payee, amount)