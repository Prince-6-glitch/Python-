
# Username Generator

print("===== USERNAME GENERATOR =====")

first_name = input("Enter your first name: ").strip().lower()
last_name = input("Enter your last name: ").strip().lower()

username = f"{first_name}_{last_name}"

print("\nYour Username:", username)

print("First 3 letters:", first_name[:3])
print("Last 3 letters:", first_name[-3:])
