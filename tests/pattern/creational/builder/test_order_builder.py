import pytest
from src.patterns.creational.builder.order_builder import OrderBuilder

def test_order_with_single_product():
    builder = OrderBuilder()
    order = (
        builder.add_product("Laptop", 1000, 1)
        .set_tax_rate(10)
        .set_shipping_cost(50)
        .build()
    )
    assert order.calculate_total() == 1150.0, "Total calculation is incorrect"

def test_order_with_multiple_products_and_discount():
    builder = OrderBuilder()
    order = (
        builder.add_product("Laptop", 1000, 1)
        .add_product("Mouse", 50, 2)
        .apply_discount(20)
        .set_tax_rate(10)
        .set_shipping_cost(50)
        .build()
    )
    assert order.calculate_total() == 1018.0, "Total calculation with discount is incorrect"

def test_order_without_tax_or_shipping():
    builder = OrderBuilder()
    order = (
        builder.add_product("Keyboard", 100, 1)
        .build()
    )
    assert order.calculate_total() == 100.0, "Total without tax or shipping is incorrect"