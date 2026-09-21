
#for loop: a block of code which run the back and back upto certain limit
s1=['Hello MIT asia','64',(845)]
for i in s1:
    print(i)

for n in range(1,896,100):
     print(n) 

#sum of numbers
addition = 0 
 
for k in range(1,11):
    addition = addition+k
print(addition)

#maximum of number using for loop
s1=[945655555555,8,7,6,5,4,0,32,1,4,5,65,4,465,7,879,321,368,999]
large=s1[0]
for i in s1:
    if large < i:
        large=i
print(large)

for coon in range(1,50):
    if coon % 23 == 0:
        break
    
    print(coon)

num=1
while num<5:
    print('J')
    num=num+1


# for l in range(10):
#     for p in range(9):
#         print(f"l={l},p={p}")

for m in range(1,10):
    for n in range(1,m+1):
        print('*', end=" ")
    print()


for b in range(0,21):
    for c in range(1,b+1):
        print(b, end=" ")
    print()

user_info={"user_name":"unknown_1",
"password":"user@123",
"email":"unknown_1@email.com",
"address":"at microsoft",
"country":"India"}
print(user_info)
print("We have delete the password and address from this user info")
info_to_delete=["password","address","contact"]
for a in info_to_delete:
    if a in user_info:
        user_info.pop(a)

print(user_info)

a=int(input("enter a number from which you want to start the sum:"))
b=int(input("enter a number from which you want to end the sum:"))
total=0
for i in range(a,b+1):
    total=total+i

print(f"The sum of numbers from 1 to 50: {total}")