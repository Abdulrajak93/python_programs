mean_arr = list(map(int, (input().split())))
add = 0
count = 0
for i in mean_arr:
    add += i
    count += 1
print(f"The mean {mean_arr} is {add//count}")