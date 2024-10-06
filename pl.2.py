a=input("enter the string:")
c=''
for ch in a:
    c+=ch
print(c)
if c==a:
    print("the given is paliandrom")
else:
    print("the not palindrom")
