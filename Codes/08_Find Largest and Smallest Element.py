# Find Largest and Smallest Element in a List without max and min
def largest(lst):
    max=lst[0]
    for i in range(1,len(lst)):
        if(lst[i]>max):
            max=lst[i]
    return max

def smallest(lst):
    min=lst[0]
    for i in range(1,len(lst)):
        if(lst[i]<min):
            min=lst[i]
    return min

n=int(input("Number of elements: "))
lst=[int(input(f"Enter element {i+1}: ")) for i in range(n)]
print("List:",lst)
print("Largest element:",largest(lst))
print("Smallest element:",smallest(lst))

