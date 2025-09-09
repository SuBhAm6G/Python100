# Develop a Python function that determines if a
# given number qualifies as a "Perfect Number".
# Example: The first perfect number is 6, because
# 1, 2, and 3 are its proper positive divisors, & 
# 1 + 2 + 3 = 6

def isPerfect(n):
    if n<=1:
        return False
    sum=0
    for i in range(1, n//2 +1):
        if(n%i ==0):
            sum+=i
    return sum==n

n=int(input("Enter Num: "))
x=isPerfect(n)
if(x==1):
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")
