#User defined function 
#def function(arg1,arg2,arg3,......,argN):
#     statement1
#     statement2

# def hello(name):
#     print(f"Hello {name},")
#     print("user defined is used when we have to use same operations without wrtiting the program again in the same script")
# name=input("enter your name:")
# hello(name)

# def add(num1,num2):
#     sum=num2+num1
#     print(f"sum is {sum}")
# add(11,32)

def odd_even(number):
    if number%2==0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."

even_odd=odd_even(56)
print(even_odd)

def arithematic_operation(num1 , num2):
    add=num1+num2
    sub=num1-num2
    mul=num1*num2
    div=num1/num2
    return add,sub,mul,div

num1=int(input("Enter first number:"))
num2=int(input("Enter secomnd number:"))

re1,re2,re3,re4=arithematic_operation(num1,num2)
print(f"Addition is {re1}")
print(f"Substraction is {re2}")
print(f"Multiplication is {re3}")
print(f"Division is {re4}")