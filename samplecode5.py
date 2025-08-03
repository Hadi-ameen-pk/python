'''name=input("Enter your name: ")
age=int(input("Enter your age: "))
print(name,age)
'''
'''
num = int(input("Enter a number: "))
j = int(input("Enter starting number: "))
k = int(input("Enter ending number: "))

for i in range(j, k + 1):
    if i%7==0:
        print(num,"*",i,"=",num*i)
'''
'''
grocery_list = ["milk", "eggs", "bread", "rice", "chicken", "cheese", "apples", ""]
items_in_pantry = ["rice", "cheese", "toilet paper"]
def remove_existing_items(grocery_list, pantry_items):
    return [item for item in grocery_list if item not in pantry_items]
def add_new_items(shopping_list, new_items):
    for item in new_items:
        if item not in shopping_list:
            shopping_list.append(item)
    return shopping_list
shopping_list = remove_existing_items(grocery_list, items_in_pantry)
new_items_needed = ["yogurt", "spinach"]
shopping_list = add_new_items(shopping_list, new_items_needed)
print("🛒 Final Shopping List:")
for item in shopping_list:
    print("-", item)
  '''

#print words starting vowels
cars = ["Alto", "Maruti", "Ertiga", "Baleno"]
for car in cars:
    if car[0].lower() in 'aeiou':
        print(car)
