#count of a string
'''
k=input("Enter a sting:")
words=dict()
for i in k:
    if i in words:
        words[i]=words[i]+1
    else:
        words[i]=1
print(words)
'''
#write a program to check weather number is palindrom or not
'''
text = input("Enter a string or number: ")

if text == text[::-1]:
    print(text, "is a Palindrome")
else:
    print(text, "is not a Palindrome")
'''
#armstrong value
'''
n = int(input("Enter the number : "))   # User inputs a number
l = len(str(n))                         # Find number of digits
sum = 0                                 # Initialize sum

for k in str(n):                        # Loop through each digit
    sum = sum + int(k)**l               # Raise digit to power of l and add to sum
if n == sum:                            # Check condition
    print(n, "is armstrong")
else:
    print(n, "is not armstrong")
'''
