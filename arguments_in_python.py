# def add(a,b):
#     add=a+b


# #positional argumemnts:- passing the argument in order to their position 
# add(10,20)

# #default arguments:-
# # def add(a,b=10):
# #     add=a+b
# #     return add
# # addition=add(1651,9)
# # print(addition)
# # addition=add(1651)
# # print(addition)

# def add(a,b=10):
#     add=a+b+c
#     print(add)
# add(22)

#*arg :-variable length positional from 1 to n
# def add(*argument):
#     return sum(argument)

# addition=add()
# print(addition)

# def student_details(id,name,*marks):
#     per=sum(marks)/len(marks)
#     print(f"{name} with id {id} has {per}%")

# student_details(42350,'Krishna Raut',98,85,78,98,95,91)

# #**kwarg :- variable length keyword argument
# def fun(id, name, *games, **marks):
#     per=sum(marks.values()) / len(marks)
#     print(f"{name} with id {id} has percentage {per}")
#     print(f"{name} plays {games}")

# fun(42350, "Krishna Raut" , "volleyball" ,m1=85,m2=87,m3=83)
# fun(42380, "Saurabh Raut" , "football", "basketball", m1=87,m2=86,m3=84)

# #doc sting :
# def fun():
#     """
#     this is doc string
#     :return: None
#     """
#     return None

# print(help(fun))

def divide(num1 , num2):
    """
    num1 :- to be divided(numrator)
    num2 :- will divide num1(denominator)
    :return: float
    """
    division = num1 / num2
    return division

print(divide(500,4))