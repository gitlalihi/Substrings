#Python | Split by repeating substring
string = input("Enter your string: ")
print("Your string is:", string)
substring=input("Enter your substring :")
result=len(string)//len(str(substring))
x=[substring]*result
print("Your split string by repeating substring is:",x)