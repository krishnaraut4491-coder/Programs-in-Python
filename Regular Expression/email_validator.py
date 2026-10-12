import re
# detail = """Krishna  krishna@gmail.com 5265689542
# Nikhil Nikhil@outlook.in 6593548485
# _wrg@faf.com
# _-@rgv.654"""

# try:
#     with open("details", "rt") as detailz:
#             data = detailz.read()
# except FileNotFoundError:
#     with open("details", "wt") as detail1:
#         detail1.write(detail)


pattern = r"\b[a-zA-Z0-9][\w.-]*@[a-zA-Z]+\.[a-zA-Z]{2,}\b"
# matching_object = re.finditer(pattern, data)

# for matches in matching_object:
#     print(matches)

data = input("Enter your email:")

if re.fullmatch(pattern, data):
    print("Email is Valid.")
else: 
    print("Email is invalid.")