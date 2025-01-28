weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday"]
purchase=int(input("Total amount: "))
items=int(input("Number of items: "))
day=str(input("Day of the week: "))

if day in weekdays:
    purchase-=purchase*0.1
else:
    purchase-=purchase*0.2

if items>5:
    purchase-=purchase*0.05

print("Total price after discount: ",purchase,"DZ")
