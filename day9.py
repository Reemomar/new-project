age = 36
txt = "My name is Jone I am {} "
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder ="I want {} prices of item {} for {} dollers"
print(myorder.format(quantity,itemno,price))

quantity = 3
itemno = 567
price = 49.95
myorder ="I want {2} prices of item {0} for {1} dollers"
print(myorder.format(quantity,itemno,price))


