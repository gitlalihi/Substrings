#Python – Test substring order
string = input("Enter your string: ")
print("Your string is:", string)
substring=input("Enter your substring:")
newstring=""
for i in string:
    if i in substring:
        newstring=newstring+i
flag=False
if(newstring.startswith(substring)):
    flag=True
print (" Is your substring ordered:",newstring)    
