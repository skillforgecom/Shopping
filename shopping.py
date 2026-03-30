total_amount = 0

item1 = input("Select first item:")
price1 = float(input("Enter price of item1:"))
#price1 =float(price1)
quantity1 = input("Enter quantity of item1:")
quantity1 = int(quantity1)
item1_total = price1 * quantity1
total_amount =total_amount + item1_total

#total_amount += item1_total

item2 = input("Select second item:")
price2 = float(input("Enter price of item2:"))
quantity2 = int(input("Enter quantity of item2:"))
item2_total = price2 * quantity2
total_amount += item2_total

print("*********************************")
print("*********************************")
print("*********************************")
print(f"{item1} X{quantity1}: ${item1_total:.2f}")
print(f"{item2} X{quantity2}: ${item2_total:.2f}")
print(f"The total amount is: ${total_amount:.2f}")
print("*********************************")
print("*********************************")
