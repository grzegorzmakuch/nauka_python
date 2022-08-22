shopShelf = ["Apple", "Orange", "Toy Car", "Banana", "Kiwi", "Pear"]
basket = []

goods = len(shopShelf) - 1
watchingGoods = 0

while watchingGoods < goods:
    print("\nYou are checking: {}".format(shopShelf[watchingGoods]))
    decision = input("Do you want it?")
    if decision == "y":
        basket.append(shopShelf[watchingGoods])
        shopShelf[watchingGoods] = " "
    watchingGoods += 1
print(" ")

print("In our store:")
for assortiment in shopShelf:
    print(assortiment, end=", ")

print("\n\nIn your basket:")
for bought in basket:
    print(bought, end=", ")