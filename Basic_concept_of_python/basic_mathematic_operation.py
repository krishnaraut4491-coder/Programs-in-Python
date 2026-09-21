'''
This is a basic python program to perform basic mathematical operations like 
addition
subtraction
multiplication 
and division.
'''
A=input('Enter the first number:')
B=input("Enter the second number:")
Addition=float(A)+float(B)
Subtraction=float(A)-float(B)
Multiplication=float(A)*float(B)
Division=float(A)/float(B) if float(B) != 0 else 'undefined (division by zero)'
print('Addition:', round(Addition,2))
print("Subtraction:",round(Subtraction,2))
print("Multiplication:",round(Multiplication,2))
print("Division:",round(Division,2) if Division != 'undefined (division by zero)' else Division)
