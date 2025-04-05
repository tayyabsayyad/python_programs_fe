class Product:
    def __init__(self, product_id, name, price, stock):
        """
        Initialize a Product with product ID, name, price, and stock.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        """
        Reduce the stock of the product by the given quantity.
        """
        if self.stock >= quantity:
            self.stock -= quantity
        else:
            raise ValueError(f"Not enough stock for {self.name}. Available: {self.stock}")

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Stock: {self.stock}"


class Customer:
    def __init__(self, customer_id, name, email):
        """
        Initialize a Customer with customer ID, name, and email.
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"Customer: {self.name}, Email: {self.email}"


class ShoppingCart:
    def __init__(self, customer):
        """
        Initialize a ShoppingCart for a specific customer.
        """
        self.customer = customer
        self.items = {}  # Dictionary to store items as {product_id: quantity}

    def add_item(self, product, quantity):
        """
        Add a product to the shopping cart.
        """
        if product.product_id not in self.items:
            self.items[product.product_id] = {'product': product, 'quantity': 0}

        if product.stock >= quantity:
            self.items[product.product_id]['quantity'] += quantity
            product.reduce_stock(quantity)
            print(f"Added {quantity} x {product.name} to the cart.")
        else:
            print(f"Error: Not enough stock for {product.name}.")

    def calculate_total(self):
        """
        Calculate the total cost of items in the shopping cart.
        """
        total = sum(item['product'].price * item['quantity'] for item in self.items.values())
        return total

    def process_order(self):
        """
        Process the order for the shopping cart.
        """
        if not self.items:
            print("Your cart is empty!")
        else:
            total_cost = self.calculate_total()
            print(f"Order processed for {self.customer.name}. Total cost: ${total_cost:.2f}")
            self.items.clear()

    def display_cart(self):
        """
        Display the items in the shopping cart.
        """
        if not self.items:
            print("The cart is empty.")
        else:
            print(f"\nShopping Cart for {self.customer.name}:")
            for item in self.items.values():
                product = item['product']
                quantity = item['quantity']
                print(
                    f"{product.name} - Quantity: {quantity}, Price: ${product.price}, Subtotal: ${product.price * quantity:.2f}")
            print(f"Total: ${self.calculate_total():.2f}")



# Create Products
product1 = Product(101, "Laptop", 1000.00, 10)
product2 = Product(102, "Smartphone", 500.00, 20)
product3 = Product(103, "Headphones", 100.00, 50)

# Create a Customer
customer = Customer(1, "Alice", "alice@example.com")

# Create a Shopping Cart for the Customer
cart = ShoppingCart(customer)

# Add Products to the Cart
cart.add_item(product1, 1)  # Add 1 Laptop
cart.add_item(product2, 2)  # Add 2 Smartphones
cart.add_item(product3, 5)  # Add 5 Headphones

# Display Cart
cart.display_cart()

# Process Order
cart.process_order()

# Display Cart After Processing
cart.display_cart()