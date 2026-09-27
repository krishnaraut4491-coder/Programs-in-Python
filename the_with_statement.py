"""
we are learing how to 
handle files using python 
or in python 
"""
 
#open(file_name,file_mode)
#modes : r,w,x,a,t,d,rt(default)=> rt,wt,xt,at,rb,wb,xb,ab
#file_name.close()

# with open("firstcode.py","rt") as first_code:
#     content = first_code.read()

# print(content)


# to check file exits or not

import os 
file_name = "firstcode.py"
if os.path.exists(file_name):
    print("File exists")
else :
    print("File does not exists")

from pathlib import Path

file_name = Path("C:/Users/Krishna Munjaji Raut/Desktop/Python/Programs in Python/firstcode.py")

if file_name.exists():
    print("File exists")
else:
    print("File does not exists")