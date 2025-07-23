def get_hello():
    return "Hello, world"

h = get_hello  # value of h is function itself
m = h()
h = get_hello() # value of h is RETURN VALUE
print(f"{h = }")

def hello():
    print("Hello, world")
    # return None

h = hello()
print(f"{h = }")

def double(x):
    return x * 2

d = double(10)
print(f"{d = }")

def c2f(c_temp):
    # ...
    f_temp = 0
    return f_temp

f = c2f(100)
