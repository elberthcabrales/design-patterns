from abc import ABC, abstractmethod

# Abstract Product
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

# Concrete Products
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        return f"Processing credit card payment of ${amount:.2f}"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        return f"Processing PayPal payment of ${amount:.2f}"

class BitcoinProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        return f"Processing Bitcoin payment of ${amount:.2f}"

# Creator (Factory)
class PaymentProcessorFactory:
    @staticmethod
    def create_processor(payment_type: str) -> PaymentProcessor:
        if payment_type == "credit_card":
            return CreditCardProcessor()
        elif payment_type == "paypal":
            return PayPalProcessor()
        elif payment_type == "bitcoin":
            return BitcoinProcessor()
        else:
            raise ValueError(f"Unknown payment type: {payment_type}")