"""
Here I used help function to get 
the information about functions in math module
like sqrt, log(base e), sin, radians
"""
import math

"""
We are taking a input to calculate
its square root, natural logarithm, 
sine of the number(in radians) 
"""
n = float(input("Enter a number: "))
print(f"Square root of {n}: {round(math.sqrt(n),5)}")
print(f"Natural logarithm of {n}: {round(math.log(n),5)}")
print(f"Sine of {n}: {round(math.sin(math.radians(n)),5)}")
"""
Here I used round function to
get only 3 floating point
"""