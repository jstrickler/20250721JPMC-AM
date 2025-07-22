print("Welcome to ticket sales\n")

while True:  # Loop "forever"
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        print("Please enter a numeric quantity: ")
        continue  # Skip rest of loop; start back at top
    if raw_quantity.lower() == 'q':
        print("goodbye!")
        break  # Exit loop

    try:
        quantity = int(raw_quantity)  # could validate via try/except
        if quantity > 100:
            print("Sorry, 100 is the maximum")
            continue
    except ValueError as err:
        print(err)
    else:
        print(f"sending {quantity} ticket(s)")
