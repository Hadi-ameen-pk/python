def calculate_total(price, tax=5):
    return price + (price * tax / 100)
print(calculate_total(100))