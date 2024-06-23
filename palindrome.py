def palindrome(s):
    if s==s[::-1]:
        return "palindrom"
    else:
        return "Not a palindrome"

#-------------------------

string= input("Enter the message:")
print(palindrome(string))
