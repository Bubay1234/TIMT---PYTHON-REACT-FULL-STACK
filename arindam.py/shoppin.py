amount = float(input("Enter shopping amount: "))

if amount >= 5000:
    discount = 25
elif amount >= 3000:
    discount = 15
elif amount >= 2000:
    discount = 10
elif amount >= 1000:
    discount = 5
else:
    discount = 0

discount_amount = amount * discount / 100
final_amount = amount - discount_amount

print("Discount:", discount, "%")
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)