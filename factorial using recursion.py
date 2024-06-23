def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

#--------------------

num=int(input())
if num<=0:
    if num<0:
        print("sorry, factorial does not work on negative numbers")
    else:
        print("The factorial of 0 is 1")
else:
    print("The factorial of",num,"is",factorial(num))

