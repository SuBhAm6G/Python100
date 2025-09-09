# Implement a function to calculate the frequency of
# duplicate elements in a list and display their
# occurrence count

def duplicates(lst):
    elements=[]
    frequency=[]
    for i in range(len(lst)):
        if lst[i] not in elements:
            x=lst.count(lst[i])
            if x>1:
                elements.append(lst[i])
                frequency.append(x)
    return elements, frequency

n=int(input("Enter number of elements: "))
lst=[float(input(f"Enter element {i+1}: "))for i in range(n)]        
d,f=duplicates(lst)
if(len(d)==0):
    print("No duplicates")
    exit(0)
for i in range(len(d)):
    print(f"Element {d[i]} occurs {f[i]} times")


