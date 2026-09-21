import random
print("Welcome to the number guessing game, we have a number tobe guess, you have 10 chances")
print("The secret number is between 1 to 50")


a=random.randint(1,50)
for i in range(0,10):
    print(f"you have {10-i} attempts left")
    number_to_guess=int(input("Enter a number between 1 to 50:"))
    if number_to_guess==a: 
        print("congrats your guess is correct!")
        break
    elif number_to_guess>a:
        print(f"Your guess is wrong!, try a number lower than {number_to_guess}")
    elif number_to_guess<a:
        print(f"Your guess is wrong!, try a number higher than {number_to_guess}")

print(F"The number was {a}, game over!")