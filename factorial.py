import math

factorial = 1

num = int(input("Write the number you would like to find the factorial of: "))

if num < 0:
    print("Sorry, you can't factorise this number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)
           
    
