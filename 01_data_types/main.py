from random import randint

answer = randint(1, 20)

guess_as_string = -1
guess = -2
counter = 1

while guess != answer:
    guess_as_string = input("Zgaduj")
    guess = int(guess_as_string)
    if guess > answer:
        print("Za duzo")
        counter += 1
    elif guess < answer:
        print("Za malo")
        counter += 1
print("Brawo, wylosowana liczba to: ", answer, ". Trafiles za ", counter, " razem")