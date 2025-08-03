grocery_list = ["Sugar", "Bread", "Fish", "Rice", "Salt", "Milk", "Tomatoes", "Onions"]
available_items = ["Bread", "Salt", "Onions"]
def filter_needed_items(grocery_list, available_items):
    to_buy = []
    for item in grocery_list:
        if item not in available_items:
            to_buy.append(item)
    return to_buy
def print_final_list(to_buy):
    print("🛒 Final Grocery List:")
    for item in to_buy:
        print(f"- {item}")
final_list = filter_needed_items(grocery_list, available_items)
print_final_list(final_list)
