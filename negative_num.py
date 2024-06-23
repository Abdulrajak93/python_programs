palindrome = []
for i in range(1, 201):
        original = i
        strcase = str(i)
        if strcase[::-1] == str(original):
            palindrome.append(i)
print(palindrome)