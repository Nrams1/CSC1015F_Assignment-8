   


def palindrome(string):
    if len(string)<=1:
        return True
    return string[0]==string[-1] and palindrome(string[1:-1])

x=input("Enter a string:\n")
if palindrome(x):
    print("Palindrome!")
else :
    print("Not a palindrome!")