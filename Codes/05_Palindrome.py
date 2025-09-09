def Palindrome(str):
    str=str.upper()
    length=len(str)
    isPalindrome=True
    for i in range (length//2 + 1):
        if(str[i]!=str[length-1-i]):
            isPalindrome=False
    return isPalindrome


str=input("Enter the word: ")
if(Palindrome(str)):
    print(str,"is a Palindrome")
else:
    print(str,"is not a Palindrome")