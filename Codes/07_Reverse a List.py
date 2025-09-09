# Reverse a List without Built-in Methods
def reverse(lst,n):
    for i in range(n//2):
        lst[i],lst[n-1-i]=lst[n-1-i],lst[i]
    return lst

n=int(input("Enter number of elements: "))
lst=[]
for i in range(n):
    lst.append(float(input(f"Enter element {i+1}: ")))
print("Original List:",lst)
print("Reversed List:",reverse(lst,n))
