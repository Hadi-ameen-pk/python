password = input("Enter password: ")

if len(password) < 6:
    print("Invalid password (too short, must be at least 6 characters)")
elif password.isdigit():
    print("Invalid password (cannot be only numbers)")
elif password.isalpha():
    print("Invalid password (cannot be only letters)")
else:
    print("Valid password")
