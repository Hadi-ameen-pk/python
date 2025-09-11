#exercise 1
password = ""
while password != "python123": password = input("Enter password: ")
else:
    print("Correct password!")

#exercise 2
numbers = [1, 2, 3, 4, 5]
target = 6
for num in numbers:
    if num == target:
        print("Number found!")
        break
else:
       print("Number not found!")

#exercise 3
secret = 7
for attempt in range(3):
    guess = int(input("Guess the secret number: "))
    if guess == secret:
        print(" Congratulations! You guessed it right.")
        break
else:
    print("Sorry, you Failed. The secret number was", secret)
