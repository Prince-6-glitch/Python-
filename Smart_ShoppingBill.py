#===== SMART SHOPPING BILL =====

print("#===== SMART SHOPPING BILL =====")

Product_name = input("Product name :")
Price = float(input("Price :"))
Quantity = int(input("Quantity :"))

subtotal =  Price*Quantity
print(f"subtotal :  {subtotal}")

discount = 10*subtotal/100
print(f"discount : {discount}")

final_price =subtotal-discount
print(f"final price : {final_price}")
Product_name = input("Product name :")
Price = float(input("Price :"))
Quantity = int(input("Quantity :"))

subtotal =  Price*Quantity
print(f"subtotal :  {subtotal}")

discount = 10*subtotal/100
print(f"discount : {discount}")

final_price =subtotal-discount
print(f"final price : {final_price}")

print("Thank You For Shopping!")