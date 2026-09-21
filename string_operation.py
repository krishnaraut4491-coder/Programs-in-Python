"""String operation in Python"""

s1='Krishna Raut'
print(s1[0])
print(s1[-1])
print(len(s1))

language='Python '
version='3.14.7'
#concatenation
#a+b/a+" "+b
print(language+' '+version)
#repetition operator
print(language*3)
dgg=input('Enter a random name:')
print(dgg)

#membership operation
#in

s1='Krishna Raut'
print("Krishna" in s1)
print('Kr' in s1)
print('qw' in s1)
print('ir' in s1)
#not in
print('qw'  not in s1)
print('python' not in s1)
print("Krishna" not in s1)
print('ir' not in s1)

#comparison of the strings
#x==x
print(s1==s1)

#removing spaces from the string
#strip() method : used to remove the leading and trailing spaces from the string
s2=' Krishna '
s3=s2.strip()
print(s3)
print(s2.strip()=='Krishna')

#replace
s1='We are learning Python'
print(s1)
print(s1.replace('Python','Java'))
s1=s1.replace('e','E',2)
print(s1)

#counting substring form string
#count()
#string.count(substring)
a1='We are learning Python. Python is fun'
a2='n'
print(a1)
print(a2)
a3=a1.count(a2)
print(a3)
print(a1.count(a2))
print(f"{a2} is repeated {a3} times in \"{a1}\"")

#Changing case of a string
#upper(),lower(),tilte(),capatilize()
a1='python 3.14.7'
print(a1.upper())
print(a1.lower())
print(a1.title())
print(a1.capitalize())
a2='We are learning Python. Python is fun'
print(a2.upper())
print(a2.lower())
print(a2.title())
print(a2.capitalize())

#Starting and Ending of a string
s1='We are learning python'
#startswith()
#string.startswith(substring)
print(s1.startswith('We'))
print(s1.startswith('W'))
print(s1.startswith('We are'))
print(s1.startswith('are'))
print(s1.startswith('we are'))
#endswith()
print(s1.endswith('python'))
print(s1.endswith('n'))
print(s1.endswith('pytho'))
print(s1.endswith('o'))
print(s1.endswith('on'))
#All operations of the string
#strip(), replace(), count(), upper(), lower(), title(), capitalize(), startswith(), endswith(),compare, membershi opperation, concatenation, repetition operator
