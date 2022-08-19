counter = 15
while counter > 0:
    if counter % 2 != 0:
        counter -= 1
        continue
    print("{}".format(counter))
    counter -= 1