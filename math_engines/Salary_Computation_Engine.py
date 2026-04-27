s = float(input("\nEnter your salary amount: "))
if s < 0:
    print("Invalid salary amount..")
else:
    l = int(input("Enter the no. of days of leave: "))
    if l >= 0 and l <= 2:
        print("Your salary is ",s)
    elif l >= 3:
        ds = s - ((l-2)*500)
        print("Your salary is ",ds)
        print()
    else:
        print("Invalid")
