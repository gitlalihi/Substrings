#Python – All substrings Frequency in String
string= input("Enter your string:")
print("Your string is:",string)

extract_substring=[string[i:j]for i in range(len(string)) for j in range(i+1,len(string)+1)]
d=dict()
for x in extract_substring:
     d[x]=string.count(x)
print("Your substrings frquency in string is :",str(d))     