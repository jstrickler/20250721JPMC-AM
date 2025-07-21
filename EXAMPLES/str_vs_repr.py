from datetime import date

today = date.today()

print(today)   # uses str(today)
print()
print(repr(today))  # uses repr(today)
print()
print(f"today = {today}")  # type 'today' twice
print(f"{today = }")  # also uses repr(today)
