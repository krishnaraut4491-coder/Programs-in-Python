print("Let's determine if a character is an alphabet and if a string is a digit.")
character=input("Enter a character: ")
if character.isalpha():
    print(f"{character} is an alphabet.")
else:
    print(f"{character} is not an alphabet.")
number=input("Enter a number: ")
if number.isdigit():    
    print(f"{number} is a digit.")  
else:
    print(f"{number} is not a digit.")