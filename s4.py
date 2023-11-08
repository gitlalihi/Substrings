#Python – Maximum Consecutive Substring Occurrence
string= input("Enter your string:")
print("Your string is:",string)
string2= input("Enter your substring")
print(" Your substring is :",string2)

word=string.split()
max_count=0
max_sub=""
for w in word:
    count=w.count(string2)
    if count>=max_count:
        max_count=count
        max_sub=max_count*string2
print("Maximum consecutive frequency is:"+ max_sub)        

