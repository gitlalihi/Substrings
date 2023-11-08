#Python – Replace all occurrences of a substring in a string
string = input("Enter your string: ")
print("Your string is:", string)

s1 = input("Enter your 1st substring from your string: ")
s2 = input("Enter your 2nd substring to replace it with: ")

string = string.replace(s1, s2)
print("Your replaced string is:", string)