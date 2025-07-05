foods = []
prices = []
Total = 0

while True:
    food = input("Enter a food to buy or press D to display the cart: ")
    if food.lower() == 'd':
        break
    else:
        price = float(input(f"Enter the price of {food}: R"))
        foods.append(food)
        prices.append(price)

# Print invoice header after exiting the input loop
print("KFC SOUTH AFRICA")
print("Copper Moon Trading Assets (Pty) Ltd")
print("KFC Rosebank")
print("Tel: 011 123 4567")
print("TAX INVOICE")
print("Vat: 47602 6230510")
print("425 Mr JazziQ")
print("--------------------------------")
print("CHK 1215       2025/06/25  12:00")
print("--------------------------------")
print("ITEMS PURCHASED:")


for food in foods:
  print(food, )
  
for price in prices:
    Total += price

print(f"Your total is: R{Total}")
print("Your Order # :")
print("305")
print("--------------------------------")
print("Thank you for shopping with us!")