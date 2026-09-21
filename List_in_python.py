'''List in Python'''

Name='Krishna'
Age=19
cgpa=7.12
student=[Name,Age,cgpa]
print(student)
print(type(student))

days_of_week=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print(days_of_week)
print(type(days_of_week))
print(days_of_week[-1]) 
print(f"last day of week is {days_of_week[-1]}")
print(f"first day of week is {days_of_week[0]}")
#length of list : number of items/elements in list
print(len(days_of_week))

#slicing of list
l1=[0,9,6,4,8,2,1,3,5,7]
print(l1)
print(len(l1))
print(l1[0:10:2]) #start:stop:step

#concatenation of list
l1=[0,1,2,3,4,5,6,7,8,9]
l2=[10,11,12,13,14,15]
print(l1+l2)
print(l2+l1)

#repetition of list
# *
a1=[1,2,3]
a2=[4,5,6]
print(a1*3)
print(a2*4)
print((a1+a2)*3)

#append() method : used to add an element at the end of the list
#adds an element at the end of the list
# list.append(item)
fruits=["Apple","Mango","Orange"]  #adds only one element at a time
print(fruits) 
fruits.append("Banana")
print(fruits)

#insert() method : used to add an element at a specific index of the list
#list.insert(index, item)
fruits.insert(3,"Banana")
print(fruits)

#extend() method : used to add multiple elements at the end of the list
#list.extend(list)
fruits=["Apple","Mango","Orange"]
print(fruits)
  # fruits.append("Banana","Pineapple") adds only one element at a time
fruits.extend(["Banana","Pineapple"])
print(fruits)
print(len(fruits))

#remove() method : used to remove an element from the list
#list.remove(item)
fruits=["Apple","Mango","Orange","Banana","Pineapple"]
print(fruits)
fruits.remove("Orange")
print(fruits)
 
#pop() method : used to remove an element from the list based on index
#list.pop(index) removes the specified index element from the list
#removes the last element from the list if index is not specified
fruits=["Apple","Mango","Orange","Banana","Pineapple"]
print(fruits)
fruits.pop(0) 
print(fruits)

#reverse() method : used to reverse the order of elements in the list
#list.reverse()
days_of_week=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print(days_of_week)
days_of_week.reverse()
print(days_of_week)

#sort() method : used to sort the elements of the list in ascending order
#list.sort()
#list.sort(reverse=True) : used to sort the elements of the list in descending order
number=[8,9,4,6,7,2,1,4,3,5] 
number.sort()
print(f"sorted list in ascending order is {number}")
number.sort(reverse=True)
print(f"sorted list in descending order is {number}")

#count() method : used to count the number of occurrences of an element in the list
#list.count(item)
number=[8,9,4,6,7,2,1,4,3,5,9,0,8,7,9,4,3,5,7,0,4,4,9,4,2,7,9,0,6,5,4,8,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0]
print(number)
item_to_count=int(input('Enter a number to count its occurences from the list: '))
a=number.count(item_to_count)
print(len(number))
print(a)
print(f"occurences of {item_to_count} in the list is {a}")

#membership operation : used to check if an element is present in the list or not
#in/not in
lanclass=["High level","Low level","Assembly level","Machine level"]
print("High level" in lanclass)
print("Java" in lanclass)
print("Python" not in lanclass)

Numbers=[10,20,20,24,45,35,64,]

#minimum(lowest) and maximum(highest) of the list
#min(list_name) and max(list_name)
minimum=min(Numbers)
maximum=max(Numbers)
print(f"Minimum of the numbers in the list is: {minimum}")
print(f"Maximum of the numbers in the list is: {maximum}")

#sum of the list
#sum(list_name)
h2=sum(Numbers)
print(f"Total of the Numbers in the list is: {sum(Numbers)}")

number=[8,9,4,6,7,2,1,4,3,5,9,0,8,7,9,4,3,5,7,0,4,4,9,4,2,7,9,0,6,5,4,8,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0]
print(f"Original list is: {number}")
print(f"Sorted list is: {sorted(number)}")
print(min(number))
print(max(number))
print(len(number))

hello=[1,2,3,4,5,6,7,8,9]
print(hello)
print(len(hello))

#nested list : a list inside a list
nested_list=[1,2,3,[4,[2,[10,[65,4]]],5,6],(10,20),[7,8,9,[12,[56,54,[25,18,[35,24]]]]]]
print(nested_list)
print(len(nested_list))
print(nested_list.index([7,8,9,[12,[56,54,[25,18,[35,24]]]]])) 
print(nested_list[3])
print(nested_list[4])
print(nested_list[3][1][1][1][0]) #printing 6 from the nested list
print(nested_list[-1][-1][-1][-1][-1][-1]) #printing 63 from the nested list
print(nested_list[-2])
#all operations of the list
#append(), insert(), extend(), remove(), pop(), reverse(), sort(), count(), in/not in, min(), max(), sum()
