#===== SMART SHOPPING BILL =====

print("#===== SMART SHOPPING BILL =====")

Product_name = input("Product name :")
Price = float(input("Price :"))
Quantity = int(input("Quantity :"))

subtotal =  Price*Quantity
print(f"subtotal :  {subtotal}")

if subtotal >= 5000:
    discount = 20 * subtotal / 100

elif subtotal >= 3000:
    discount = 10 * subtotal / 100

elif subtotal >= 1000:
    discount = 5 * subtotal / 100
else:
    discount = 0

print(f"discount : {discount}")

final_price =subtotal-discount
print(f"final price : {final_price}")

print("Thank You For Shopping!")
print("Visit Again")

    