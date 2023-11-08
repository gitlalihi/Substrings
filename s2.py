#Python – Substring presence in Strings List
string=input("Enter your list of strings seperated by a coma:").split(",")
print(string)
substring= input("Enter your substring in the list seperated by a coma:").split(",")
print(substring)
def present_substring(string,substring):
    if substring in string:
        return True
    else:
        return False
print("Your substring presence in list is :",present_substring(string,substring))    
