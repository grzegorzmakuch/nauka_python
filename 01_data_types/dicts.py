ages = {"grzegorz": 42, "maja": 11, "martyna": 39}
guitars = dict(ibanez=5, chapman=6)
print(ages)
print(guitars)
# print("Grzegorz ma {} lat".format(ages["grzegorz"]))
ages['nutka'] = 6
print(ages)

# del ages -- usuwa caly obiekt
# ages.pop("nutka") -- usuwa dany wpis
print(ages.keys())
print(ages.values())

namesList = list(ages.keys())
print(type(namesList))
print(ages["grzegorz"])