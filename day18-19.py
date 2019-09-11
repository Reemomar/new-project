Material=["Cotton" ,"Glass","Plastic"]
Material.remove("Glass")
print(Material)

Material=["Cotton" ,"Glass","Plastic"]
del Material[2]
print(Material)


Material=["Cotton" ,"Glass","Plastic"]
mymaterial =Material.copy()
print(mymaterial)

Material=["Cotton" ,"Glass","Plastic"]
Material.clear()
print(Material)

tuple = ("java" ,"python","swift")
if "python" in tuple:
    print("yes, 'pyhon' in the tuple")
