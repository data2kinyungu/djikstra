import random
number = random.randrange(1,10)

#your_guess = input("Enter a number: ")
#guess = int(your_guess)
guess = int(input("Enter a number: "))

while number != guess:
    if guess < number:
        print("Too low")
        guess = int(input("Enter a number again: "))
    elif guess > number:
        print("Too high")
        guess = int(input("Enter a number again: "))
    else:
        break

print("Hurray!!!, you guessed it right!!")
