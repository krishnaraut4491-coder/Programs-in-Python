"""
Here we are writing a program in which we will 
take input of any number and give factorial 
of that number as output. Using loop and Recursion.
"""
# # using loop
# def facto(factorial):
#     number_factorial = 1
#     while factorial > 1:
#         number_factorial  = number_factorial  * factorial
#         factorial = factorial - 1
#     return number_factorial 

# factorial = int(input("Enter a number:"))
# print(f"Factorial of {factorial} is:")
# print(facto(factorial))

#Using recursion
def fact(factorial):
    if factorial == 1:
        return 1
    else:
        factorial_number = factorial * fact(factorial - 1)
    return factorial_number 

factorial = int(input("Enter a number: "))
print(f"Factorial of {factorial} is: ")
print(fact(factorial))