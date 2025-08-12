#division by zero
a,b=32,0
try:
    print(a/b)
except ZeroDivisionError:
    print(Divided by zero)
#type error
try:
    print(a/"7")
except TypeError:
    print("TypeError")
#Key error
g={"name":"Hadi"}
try:
    print(g['place'])
except KeyError:
    print("Key not found")