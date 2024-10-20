a=input("enter the string:")
c=''
for ch in a:
    c+=ch
print(c)
if c==a:
    print("the given string is a palindrome")
else:
    print("the given string is not a palindrom")
