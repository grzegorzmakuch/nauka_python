myTuple = (10.4, 40.5, 123)
myList = [1,2,3,4,5]
myString = "My new string"

# print("Typ danych myTuple {}".format(type(myTuple)))
print("Adres tuple w pamieci {}".format(id(myTuple)))
print("Adres lista w pamieci {}".format(id(myList)))
print("Adres string w pamieci {}".format(id(myString)))

print("Typ wskaznika to {}".format(type(id(myTuple))))

x, y, z = myTuple
print("Wspolrzedne: x = {}, y = {}, z = {}".format(x, y, z))
print("Wspolrzedne (py2.0) : x = %s, y = %s, z = %s" % myTuple)