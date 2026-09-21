#Tuple in python
#syntax: tuple_name=(value1,value2,value3)
t1=(1,2,(3,4),[5,6],7)
t2=(6,4,2)
t4=(4,9,6,1,5)
#length of tuple
print(len(t1))
#indexing of tuple
print(t1.index(7))
print(t1[3])

#slicing in tuple
print(t1[0:4:1])

#concatenation of the tuple
#joining of the two string  
t3=t1+t2
t5=t2+t4
print(t3,t5)

#repetition of the tuple
#*
print(t2*2)

#memebership operator in tuple
#in/not in
print(4 in t3)
print(5 not in t2)
print(39 in t3)

#comparison in tuple
print(t1==t2)

#sum() of element in tuple
print(sum(t5))

#min()
print(min(t5))

#max()
print(max(t5))
