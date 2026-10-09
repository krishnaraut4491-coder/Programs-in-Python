import re

message = "the current version of python is 354.14.8"

matching_object = re.search("[0123456789]", message)
print(matching_object)

matching_object = re.search("[0123456789][0-9]", message)
print(matching_object)

matching_object = re.search("[0123456789].[0-9][0-9]", message)
print(matching_object)

matching_object = re.search("[0123456789].[0-9]", message)
print(matching_object)
# . matches any character except new line character(\n)


matching_object = re.search("[a-z].[a-z]", message)
print(matching_object)