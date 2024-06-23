mode_arr = list(map(int, (input().split())))
_dict = {}
for i in mode_arr:
    if i not in _dict:
        _dict[i] = mode_arr.count(i)
max_val = max(_dict.values())
for key, value in _dict.items():
    if value == max_val:
        print(f"Mode of the array is {key}")
        break
