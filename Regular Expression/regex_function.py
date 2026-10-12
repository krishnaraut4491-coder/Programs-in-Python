import re   

# # match()
# s1 = "here are functions of regex in python"

# matching_object = re.match("[a-z]{3}", s1)
# print(matching_object)

# #findall()
# phones = "krishna-1231254635, nikhil-6524865329, shivraj-7598621530, landline-58462847"

# patern = "[0-9]{10}"
# print(re.findall(patern, phones))

# patern = "[0-9]+"
# print(re.findall(patern, phones))


# phones1 = """krishna-1231254635, nikhil-6524865329, shivraj-7598621530, 
# landline-58462847, number-4415411644854412"""

# patern = r"[0-9]{7,}"
# print(re.findall(patern, phones1))

# patern = r"[0-9]{7,15}"
# print(re.findall(patern, phones1))

# # \b => matches the word boundary, it is used to find the exact word in the string
# patern = r"\b[0-9]{7,15}\b"
# print(re.findall(patern, phones1))

# # finditer() => returns an iterator object, which can be used to iterate over all the matches in the string
# patern = r"[0-9]{7,15}"
# match_obj_iter = re.finditer(patern, phones1)

# for phones in match_obj_iter:
#     print(phones)

# #sub()
# s1 = "Sunday, Monday, Tuesday, Day, Monday, Sunday, day, Saturday, Friday"
# print(re.sub("Sunday", "Saturday", s1))

# print(re.sub("Sunday", "Saturday", s1, count = 1))
# print(s1)
# print(re.search("Monday", s1))
# s2 = re.sub(s1[25:31], "Wednessday", s1)
# s3 = re.sub("Wednessday","Monday", s2, count = 1)
# print(s2)
# print(s3)

# pattern = r"\bDay\b"
# replacewith = "Night"
# changes = re.sub(pattern, replacewith, s1, flags = re.IGNORECASE)
# print(changes)

# # re.compile() => compiles a regular expression pattern into a regular expression object, which can be used for matching using its match(), search() and other methods
phones = "krishna-1231254635, nikhil-6524865329, shivraj-7598621530, landline-58462847"
pattern = r"\d{10}"
phones_cache = re.compile(pattern)
print(phones_cache)
print(re.findall(phones_cache, phones))