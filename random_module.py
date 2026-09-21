import random

#random() :print a random float value between 0.00 to 1.00(excluded)
# print(random.random())

#randint(a,b) : gives random integer between a and b(a and b both are included)
print(random.randint(1,10))

#choice(sequence)
number=[65,12,48,8,3,4,2,5,6,5]
print(random.choice(number))

#shuffle(sequence)
fruits=["apple","banana","mango"]
random.shuffle(fruits)
print(fruits)