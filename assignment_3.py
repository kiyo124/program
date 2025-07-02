#Task 1
a=int(input("enter number to find factorial:"))
def fact(b):
    if b<2:
        return 1
    else:
        return b*(fact(b-1))
fa=fact(a)
print("factorial of number is: ",fa)
#task 2
import math
a=int(input("enter a number"))

print("Square Root ",math.sqrt(a))
print("logarithm ",math.log(a))
print("Sine ",math.sin(a))
