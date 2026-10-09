import re

s1 = "Python is programming language. Python3.14.8 is the current version."
#[A-Z],[a-z]

patern = r"[A-Z][a-z][a-z]"

print(re.search(patern, s1))

#\d and \D
#\d matches 1 digit character same as [0-9]
pat = "[a-z][a-z][a-z]\d"
print(re.search(pat, s1))

#\D matches any non-digit character, It is similar to [a-z]
pat = "[a-z][a-z][a-z]\D"
print(re.search(pat, s1))

s2 = """Hi, this is 
Krishna Raut
from jnv and mit
"""
#\s and \S
#\s matches any whitespace character also new line character,\t
pat = "[a-z][a-z][a-z]\s"
print(re.search(pat, s2))

#\S => exactly opposite to the \s, matches any character except space,\n and \t
pat = "[a-z][a-z][a-z]\S"
print(re.search(pat, s2))

#\w matches [a-z],[A-Z], [0-9]
pat = "[a-z][a-z][a-z]\w"
print(re.search(pat, s2))

#\W => exact oppposite of \w, except a non alphanumeric
pat = "[a-z][a-z][a-z]\S"
print(re.search(pat, s2))