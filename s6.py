#Python – Possible Substring count from String
string= input("Enter your string:")
print("Your string is:",string)
string2= input("Enter your substring")
print(" Your substring is :",string2)
string2=set(string2)
max_count=10000
for i in string2:
    x=string.count(i)
    if x<max_count:
        max_count=x
print("Your possible substring count is :", max_count  )      
