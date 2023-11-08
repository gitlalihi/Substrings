#Python – Remove after substring in String
string = input("Enter your string: ")
print("Your string is:", string)
substring=input("Enter your substring :")
result=string[:string.index(substring)+len(substring)]
print("Your result after removing the string is ",result)
