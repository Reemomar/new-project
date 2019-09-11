thistuple = ("apple","bnana","cherry")
print(thistuple)

thistuple = ()
print(thistuple)

thistuple = (3,)
print(thistuple)

thistuple = (3,1.3,4.1,7)
print(thistuple)

thistuple = ("Ahmad",1.1,4,"بايثون")
print(thistuple)
thistuple = ("apple","bnana","cherry")
print(thistuple[1])

thistuple = ("apple","bnana","cherry")
for x in thistuple:
    print(x)

thistuple = ("apple","bnana","cherry")
thistuple[3] = "orang" #this will raise an error
print(thistuple)

thistuple = ("apple","banana","cherry","oravg")
print(thistuple [0:3])
