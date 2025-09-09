# Count the frequency of each character in a string.
def freq(str):
    chars=[]
    frequency=[]
    for i in range(len(str)):
        if str[i] in chars:
            continue
        else:
            chars.append(str[i])
    for i in range(len(chars)):
        count=0
        for j in range(len(str)):
            if(str[j]==chars[i]):
                count+=1
        frequency.append(count)
    return chars, frequency

str=input("Enter string: ")
c, f=freq(str)
for i in range(len(c)):
    print(f"Character '{c[i]}' occurs {f[i]} times")
