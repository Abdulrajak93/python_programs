n = int(input("Enter the value"))
if n == 0:
    print(" 0th term is not defined")
array1 = [3, 7, 11, 5]
difference = abs(array1[0] - array1[1])
print(f"The nth term is {(difference * n) - 1}")