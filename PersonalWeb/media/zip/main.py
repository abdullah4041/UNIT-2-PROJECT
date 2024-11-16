price = 2.99
quantity = 3
tax_rate = 7.5 / 100  

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Price of item: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate * 100}%")

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
