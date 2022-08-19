myList = [1, 2, 3, 4, 5, 6]
myList2 = [True, "dwa", 3]

myList.append("weeee")
print(myList)

myList.insert(2, "dodane")
print(myList)
lastIndex = len(myList) - 1
print("Ostatni znak to : {}".format(myList[lastIndex]))

myList.remove(myList[2])
print(myList)