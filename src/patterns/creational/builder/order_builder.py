# src/patterns/creational/builder/order_builder.py

class Order:
    def __init__(self):
        self.products = []
        self.discount = 0
        self.tax_rate = 0
        self.shipping_cost = 0

    def add_product(self, product_name: str, price: float, quantity: int = 1):
        """Add a product to the order."""
        self.products.append({"name": product_name, "price": price, "quantity": quantity})

    def apply_discount(self, discount: float):
        """Apply a discount to the order."""
        self.discount = discount

    def set_tax_rate(self, tax_rate: float):
        """Set the tax rate for the order."""
        self.tax_rate = tax_rate

    def set_shipping_cost(self, shipping_cost: float):
        """Set the shipping cost for the order."""
        self.shipping_cost = shipping_cost

    def calculate_total(self):
        """Calculate the total cost of the order."""
        subtotal = sum(product["price"] * product["quantity"] for product in self.products)
        discount_amount = subtotal * (self.discount / 100)
        tax_amount = (subtotal - discount_amount) * (self.tax_rate / 100)
        total = subtotal - discount_amount + tax_amount + self.shipping_cost
        return total

    def __str__(self):
        return (
            f"Order Details:\n"
            f"Products: {self.products}\n"
            f"Discount: {self.discount}%\n"
            f"Tax Rate: {self.tax_rate}%\n"
            f"Shipping Cost: ${self.shipping_cost:.2f}\n"
            f"Total: ${self.calculate_total():.2f}"
        )


class OrderBuilder:
    def __init__(self):
        self.order = Order()

    def add_product(self, product_name: str, price: float, quantity: int = 1):
        self.order.add_product(product_name, price, quantity)
        return self

    def apply_discount(self, discount: float):
        self.order.apply_discount(discount)
        return self

    def set_tax_rate(self, tax_rate: float):
        self.order.set_tax_rate(tax_rate)
        return self

    def set_shipping_cost(self, shipping_cost: float):
        self.order.set_shipping_cost(shipping_cost)
        return self

    def build(self):
        return self.order