base_price=int(input("enter the basic salary of an employee:"))
print("basic salary:",base_price)
if (base_price<25000):
    da=base_price*80/100
    hra=base_price*20/100
    print("Dearness Allowance:",da)
    print("House Rent Allowance:",hra)
    gross=base_price+da+hra
    print("Gross salary:",gross)
elif(base_price>=25000 & base_price<40000):
    da=base_price*90/100
    hra=base_price*25/100
    print("Dearness Allowance:",da)
    print("house rent allowance:",hra)
    gross=base_price+da+hra
    print("Gross salary:",gross)
else:
    da=base_price*95/100
    hra=base_price*30/100
    print("dearness allowance:",da)
    print("house rent allowance:",hra)
    gross=base_price+da+hra
    print("Gross salary:",gross)
