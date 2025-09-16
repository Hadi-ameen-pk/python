text = input("Enter a string: ")

# 1. First and last character
print("First and Last:", text[0], text[-1])

# 2. Reverse the string
print("Reversed:", text[::-1])

# 3. Count occurrences of a character
char = input("Enter a character to count: ")
print("Occurrences of", char, ":", text.count(char))

# 4. Replace spaces with underscores
print("With underscores:", text.replace(" ", "_"))

# 5. Check if palindrome
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
