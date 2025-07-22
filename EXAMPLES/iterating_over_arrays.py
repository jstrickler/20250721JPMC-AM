fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon']

# for VAR in ITERABLE:
# for VAR, VAR, ... in ITERABLE:
for fruit in fruits:
    if fruit.startswith('a'):
        continue
    print(fruit)
print()

