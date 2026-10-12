import re


s1 = "The Python is programming language. Python3.14.8 is the current version."

patern = "[a-z]{4}"
print(re.search(patern, s1))

patern = "[A-Z][a-z]{5}"
print(re.search(patern, s1))

patern = "[A-Z][a-z]{2,5}"
print(re.search(patern, s1))

#+ => matches 1 or more repetitions of the previous pattern
patern = "[A-Z][a-z]+"
print(re.search(patern, s1))

#? => matches 0 or 1 repetition of the previous pattern
patern = "[A-Z][a-z]?"
print(re.search(patern, s1))
 
# * => matches 0 or more repetitions of the previous pattern
patern = "[A-Z][a-z]*"
print(re.search(patern, s1))
