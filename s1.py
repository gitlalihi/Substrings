#Check if String Contains Substring in Python
string=str(input(" Enter your string:"))
substring= str(input("Enter your substring:"))
if substring in string:
    print ("Your substring is present in the string")
else:
    print("Your substring is not a part of your string")