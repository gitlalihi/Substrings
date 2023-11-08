#Python | Remove substring list from String
string = input("Enter your string: ")
print("Your string is:", string)
substring=input("Enter your substring seperated by a comma :").split(",")
for i in substring:
    string=string.replace( i  , ' ')
print("Removed substring list from string is", string)    
