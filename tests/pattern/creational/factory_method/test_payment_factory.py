import pytest
from src.patterns.creational.factory_method.payment_processor import (
    PaymentProcessorFactory,
    PaymentProcessor,
)

def test_credit_card_processor():
    processor = PaymentProcessorFactory.create_processor("credit_card")
    assert isinstance(processor, PaymentProcessor), "Processor should be an instance of PaymentProcessor"
    result = processor.process_payment(100.0)
    assert "credit card" in result, "Should process credit card payment"

def test_paypal_processor():
    processor = PaymentProcessorFactory.create_processor("paypal")
    assert isinstance(processor, PaymentProcessor), "Processor should be an instance of PaymentProcessor"
    result = processor.process_payment(50.0)
    assert "PayPal" in result, "Should process PayPal payment"

def test_bitcoin_processor():
    processor = PaymentProcessorFactory.create_processor("bitcoin")
    assert isinstance(processor, PaymentProcessor), "Processor should be an instance of PaymentProcessor"
    result = processor.process_payment(200.0)
    assert "Bitcoin" in result, "Should process Bitcoin payment"

def test_unknown_processor():
    with pytest.raises(ValueError, match="Unknown payment type"):
        PaymentProcessorFactory.create_processor("unknown")