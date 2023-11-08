#Python – Longest Substring Length of K
string = input("Enter your string: ")
print("Your string is:", string)
k=input("Enter the charachter you want to find the longest substring length")
count=0
maxresult=0
for i in range (len(string)):
    if string[i]==k:
        count=count+1
    else:
        count=0
    maxresult=max(maxresult,count)
print("Your longest substring length of the charachter is :",maxresult)            