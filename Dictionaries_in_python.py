#Dictionaries in python
#comma separated key-value pairs enclosed within {}
#{key1:value1,key2:value2,.....}
#keys cannot be duplicate and most recent value will be displayed
student_marks={"Krishna":30,"Nikhil":40,"Shivraj":35}
student_marks_sem1={'Rushikesh':44,'Aniket':39}
print(student_marks,type(student_marks))
print(len(student_marks))
print(student_marks['Krishna'])
# print(student_marks['Vedant']) : This will give an error
student_marks['Krishna']=43
print(student_marks)
student_marks['Mahesh']=30
print(student_marks)

#get()
print(student_marks.get('Krishna'))
print(student_marks.get('Vedant')) #This doen't give an error instead it gives 'None'
print(student_marks.get('Vedant',34))

#Membership operator
#in/not in
print(43 in student_marks)
print(40 in student_marks)
print('Krishna' in student_marks) #Only gives True if key is present

#update()
student_marks.update(student_marks_sem1)
print(student_marks)

#pop()
student_marks.pop('Shivraj')
print(student_marks)

d1={(1,3,5):9,(1,2,1):4}
print(d1)
#key cannot be a list or set: mutable datatype
#key can be: str,int,tuple,float,bool: immutable datatype
#values can be any datatype
d2={'id':49179,'name':'Krishna','marks':{'em&la':12,'deca':13,'ds':9}}
print(d2)
print(d2['marks']['deca'])

#keys()
#use keys() to only fetch keys
print(student_marks.keys(),type(student_marks.keys()))
#values()
#use values() to only to fetch values
print(student_marks.values(),type(student_marks.values()))
#items()
print(student_marks.items(),type(student_marks.items()))

#shallow deep copy
import copy
#shallow copy
p1=[1881,61,16,1,[84,76,4,6],25,7]
p2=copy.copy(p1)
print(p2)
print(id(p1))
print(id(p2))
print(id(student_marks))
p1[2]=10
p1[4][2]=100
print(f'd2=>{p1}',id(p1))
print(f'p2=>{p2}',id(p2))

#deep copy
p3=[54,42,5,4,[7,876,653,62],254,4,65]
print(p3)
p4=copy.deepcopy(p3)
print(p4)
print(id(p3))
print(id(p4))
print(id(student_marks))
p3[2]=565
p3[4][2]=1152
print(f'p3=>{p3}',id(p3))
print(f'p4=>{p4}',id(p4))

#same thing applicable for dictionaries