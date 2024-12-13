Store class to represent a store
class Store:
  def __init__(self, name):
    self.name = name
    self.products = []
  def add_product(self, product):
    self.products.append(product)
  def remove_product(self, product):
    self.products.remove(product)
  def list_products(self):
    print(f"Products in {self.name}:")
    for product in self.products:
      print(product)
  def calculate_bill(self, items):
    total = 0
    for item in items:
      for product in self.products:
        if product.name == item:
          total += product.price
          break
    return total
class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price
  def __str__(self):
    return f"{self.name} - ${self.price}"
store = Store("My Store")
store.add_product(Product("Apple", 1.99))
store.add_product(Product("Banana", 0.99))
store.add_product(Product("Orange", 1.49))
# List all products in the store
store.list_products()
# Calculate the bill
items = ["Apple", "Banana", "Orange"]
total_bill = store.calculate_bill(items)
print("Total bill:", total_bill)
