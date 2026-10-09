#Regular Expresion(RegEx)
import re

message = ("version of python is 3.14.8")

# print("python" in message) 
# print("14" in message)
# print("3" in message)
# print("3.13" in message)
# print(message.find("v"))

help(re)

'''
re.search(regex_patern,string) => return a match object when match is found, else return None 
'''

# x = input("Enter what u want to find from message: ")
# # print(re.search(x, message))
# # x => need to be search from message 
# if re.search(x,message):
#     print("Found!")
# else :
#     print("Not found.")   