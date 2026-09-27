"""
we are learing how to handle 
files using python or in
python
"""
#open(file_name, file_mode)
#modes :- r,w,x,a,t,d,rt(default)=> rt,wt,xt,at,rb,wb,xb,ab
#file_name.close()
#x => to create a file. If file already created give error
#w => to write/overwrite file and also create a file
#r => to read the info in the file 
#a => to write at end of the file also create the file   
#t => text file 
#b => binary file

# new = open("file_handeling_in_python.py","wt")

# new.write("\"\"\"\nwe are learing how to \nhandle files using python \nor in python \n\"\"\"\n ")
# new.write("\n#open(file_name,file_mode)\n")
# new.write("#modes : r,w,x,a,t,d,rt(default)=> rt,wt,xt,at,rb,wb,xb,ab\n")
# new.write("#file_name.close()\n")
# new.close()

# read_file = open("Sets_in_python.py","rt")

# lines = read_file.readlines()
# content = read_file.read()
# print(len(content))
# print(content)
# print(type(content))
# print(lines)
# print(type(lines))
# for line in lines:
#     print(line.rstrip("\n"))
#if empty string is given means end of list or file are ended
# read_file.close()

#try except to handle error while runtime
try:
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    print(a/b)
except ZeroDivisionError:
    print("The denominator should not be 0")
except ValueError:
    print("Enter a number only")