#Python – String till Substring
string = input("Enter your string: ")
print("Your string is:", string)
substring=input("Enter your substring:")
result=string.partition(substring)[0]
print(" The string till your entered substring is :",result)