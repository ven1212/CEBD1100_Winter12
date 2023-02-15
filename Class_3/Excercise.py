ct = input("Custumer type - R/W:")

ct = ct.lower() # converts to lowercase

it = float(input("Invoice total:"))
dis = 0.0 # the discount to be determined.



if ct == "r":
    if it >= 100.00 and it < 250:
        dis = 0.1
    elif it >= 250.00:
        dis = 0.2

elif ct == "w":
    if it < 500.00:
        dis = 0.4
    elif it >= 500.00:
        dis = 0.5


else:
    print("Code not valid.")

print(f"Discount determined is {dis}")