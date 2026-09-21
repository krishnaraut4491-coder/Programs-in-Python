#Sets in Python
set1={10,"Krish",3.5}
print(set1)
#Sets are non sequential
#Sets doesn't have indexing or operation 
print(len(set1))
print(type(set1))
set1=list(set1)
print(set1)
g6=type(set1)
print(g6)
#concatenation of sets not possible
print(set1)
set2={1,2,3,4,5,6,7,8,9,0}
print(set2)
set2=list(set2)
print(set2)
print(type(set2))
l1=[2,2,4,3,3,4,2]
print(l1)
print(type(l1))
l1=set(l1)
print(l1)
print(type(l1))

#add()
set3={56,5,6,5,8,2,5,7,2,8,6,5,4}
print(set3)
set3.add(55)
print(set3)
#remove()
set3.remove(56) #gives an error when element is not present in set
print(set3)
#disard() :don't give error when element is not present in set and we wan't to remove it
set3.discard(55)
print(set3)

#mathematical operation on set
#union of set
student_data1={20,50,50,60,40,20}
print(student_data1)
student_data2={60,40,50,40,20,30}
print(student_data2)
student_data=student_data1.union(student_data2)
print(student_data)

#intersection of sets
student_data=student_data1.intersection(student_data2)
print(student_data)

#frozen sets: Immutable sets
s1={5,6,4,2,5}
print(s1,type(s1))
print(frozenset(s1),type(frozenset(s1)))
s1=type(s1)
print(type(s1))
fs1={654,65,1,6,5652,23,62,51,}
print(fs1)
fs2={645,498,96,56,5,6,62,5,51,1}
print(fs2)
print(f"Union of the sets is {fs1|fs2}")
print(f"Intersection of the sets is {fs1&fs2}")
print(f"Difference of the sets is {fs1-fs2}")
