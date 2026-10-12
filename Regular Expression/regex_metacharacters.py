import re

message = "the current version of python is 354.14.8"

# matching_object = re.search("[0123456789]", message)
# print(matching_object)

# matching_object = re.search("[0123456789][0-9]", message)
# print(matching_object)

# matching_object = re.search("[0123456789].[0-9][0-9]", message)
# print(matching_object)

# matching_object = re.search("[0123456789].[0-9]", message)
# print(matching_object)
# # . matches any character except new line character(\n)


# matching_object = re.search("[a-z].[a-z]", message)
# print(matching_object)

import re
# # ^  - caret => matches only at the beginning 

# matching_object = re.search("^[0123456789].[0-9]", message)
# print(matching_object)

# $ => matches end of string

# matching_object = re.search("[0123456789].[0-9]$", message)
# print(matching_object)

# group - () => find the exact element in it


matching_object = re.search(r"(on)\s\S", message)
print(matching_object)
print(message[17:21])