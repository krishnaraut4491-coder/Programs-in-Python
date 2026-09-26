#LAMBDA 
"""
Syntax 
lamda argument : expression
"""
# add = lambda a : a+1
# addition = add (10)
# print(addition)

# add = lambda a , b: a+1+b
# addition = add (10,14)
# print(addition)

#filter and map function
#filter(function,sequence)
seq = [1,2,3,4]
odd = lambda x : True if x % 2 !=0 else False
odd_from_seq = filter(odd,seq)
print(odd_from_seq)
print(f"odd numbers form the sequence are {list(odd_from_seq)}")
mapped = map(lambda x : True if x % 2 !=0 else False, seq)
print(f"map output : {list(mapped)}")
square = map(lambda x : x ** 2, seq)
print(f"map output : {list(square)}")
