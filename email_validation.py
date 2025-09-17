import re
pattern=r"[a-z0-9]+@[a-zA-Z]+\.(com|in|org)"
email=input("Enter email: ")
if bool(re.search(pattern, email)):
    print("Valid email")
else:
    print("Invalid email")
