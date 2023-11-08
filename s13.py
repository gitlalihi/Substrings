#Python | Remove Redundant Substrings from Strings List
string = input("Enter your string: ")
print("Your string is:", string)

string2 = input("Enter your  2nd string: ")
print("Your  2nd string is:", string2)

newstring=""
for i in string:
    if i not in string2:
       newstring=newstring+i
for j in string2:
    if i not in string:
        newstring=newstring+j
print("Resulting string after removing redundant substrings:", newstring)        


