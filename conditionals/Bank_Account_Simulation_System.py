ia = int(input("Enter the intial amount: "))
if ia < 1000:
    print("Intial amount should be greater than 1000")
else:
    print("\n--------- MODE OF TRANSACTION ---------")
    print("\t\t1. Deposit\n\t\t2. Withdraw")
    print("---------------------------------------\n")
    choice = int(input("Enter your mode of transaction: "))
    if choice == 1:
        da = int(input("\nEnter Deposit amount: "))
        if da < 500:
            print("Deposit amount should be greater than 500")
        else:
            ta = ia+da
            print("Amount deposited successfully...!\nBalance amount: ",ta)
    elif choice == 2:
        wa = int(input("Enter Withdrawal amount: "))
        if wa < 1:
            print("Invalid amount")
        else:
            ta = ia-wa
            if ta < 1000:
                print("Amount cannot be withdrwn...\nThe balance amount should be greater than 1000")
            else:
                print("Amount withdrawn successfully...!\nBalance amount: ",ta)
    else:
        print("Invalid choice..")
