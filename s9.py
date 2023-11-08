#Python – Extract Indices of substring matches
string = input("Enter your string: ").split(",")
print("Your string is:", string)
substr=input("Enter your substring:")

s1=string.index(substr)
print("Your extracted string indices is:",s1)