# This program gets an item's original price and
# calculates its sale price, with a 20% discount.

# Get the item's original price.
original_price = float(input("Enter the item's original price: "))

# Calculate the amount of the discount.
discount = original_price * 0.2

# Calculate the sale price.
sale_price = original_price - discount

# Display the receipt.
print('The original price is', original_price,
      "with 20% discount the sale price is:", sale_price,
      "You have saved", discount)
