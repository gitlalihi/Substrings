#Python – Maximum occurring Substring from list
string=input("Enter your  strings ")
print(string)
substring=input("Enter your substring sepersrted by a comma :").split(",")
print(substring)
newstring=[]
for i in substring:
    newstring.append(string.count(i))
m=max(newstring)
r=substring[newstring.index(m)]   
print("Your maximum occuring substring from list is :"+ str(r))

