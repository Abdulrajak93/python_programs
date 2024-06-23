_dict = { 1:True, 2:True, 3:True, 5:False, 6:False}
for i in _dict:
    if _dict.get(i) == False:
        print(f"{i} is {_dict[i]}")
        