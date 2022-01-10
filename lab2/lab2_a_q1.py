sellingPrice = float(input("Enter the selling price: "))
buyingPrice = float(input("Enter the buying price: "))

if sellingPrice > buyingPrice:
    print("You have profit in trading of this item")
else:
    print("You have loss in trading of this item")
