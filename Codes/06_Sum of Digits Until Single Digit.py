# Keep summing digits until you get a single digit.
def func(num):
    temp=str(num)
    while(len(temp)!=1):
        sum=0
        for i in range (len(temp)):
            sum+=int(temp[i])
        temp=str(sum)
    return int(temp)

num=int(input("Enter a number: "))
if (num<0):
    num=-num
    print('-',func(num))
else:
    print(func(num))
