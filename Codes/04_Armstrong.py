def Armstrong(n):
    a=n
    pow=len(str(n))
    sum=0
    while(a):
        rem=a%10
        sum+=rem**pow
        a=a//10
    return sum==n
n=int(input("Enter a number: "))
if(Armstrong(n)):
    print(n,"is an Armstrong number")
def is_armstrong(n):
    """Checks if a number is an Armstrong number."""
    temp_num = n
    order = len(str(n))
    total = 0
    while temp_num > 0:
        digit = temp_num % 10
        total += digit ** order
        temp_num //= 10
    return total == n

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(n,"is not an Armstrong number")
    print(f"{num} is not an Armstrong number")
