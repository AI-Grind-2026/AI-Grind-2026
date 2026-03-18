import random
number = random.randint(1, 10)
attemps = 0
maximal = 3
while attemps < maximal:
Guess = int(input("Guess the number! (1-10)"))
if Guess == number:
    print("Congratulations! You guessed the number.")
elif Guess > number:
    print("Too high! Try again")
elif Guess < number:
    print("Too low! Try again!")
else:
    print("well... you didnt guess the number but at least you tried")