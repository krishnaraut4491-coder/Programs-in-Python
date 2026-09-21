num=int(input('Enter a number:'))
if num % 2 == 0:
    print('number is even')
else:
    print('Number is odd')

# ternary operator: one line if else block
# true-condition if-condition false-condition
print('number iss even') if num%2==0 else print('number is odd')