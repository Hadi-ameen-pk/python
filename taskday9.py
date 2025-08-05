total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)

numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        print(num)

for i in range(1, 11):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()
