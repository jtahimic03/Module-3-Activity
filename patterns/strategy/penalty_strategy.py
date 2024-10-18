from patterns.strategy.payment_strategy import PaymentStrategy
from payee.payee import Payee
from billing_account.billing_account import BillingAccount

class PenaltyStrategy(PaymentStrategy):
    
    def process_payment(self, account: BillingAccount, payee: Payee, amount: float) -> str:

        account.deduct_balance(payee, amount)
        
        balance = account.get_balance(payee)

        if balance <= 0.0:
            return f"Processed payment of ${amount:,.2f}. New balance: ${balance:,.2f}"
        else:
            return f"Insufficient payment. Added penalty fee of $10.00. New balance: ${balance:,.2f}"