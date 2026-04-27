print("GRADE CALCULATION\n")
m1 = float(input("Enter mark 1: "))
m2 = float(input("Enter mark 2: "))
m3 = float(input("Enter mark 3: "))
m4 = float(input("Enter mark 4: "))
m5 = float(input("Enter mark 5: "))
tot = m1+m2+m3+m4+m5
p = tot/5
print("\nPercentage : ",p)
if p >= 90 and p <= 100:
    print("Grade : 'O'")
elif p >= 80:
    print("Grade : 'A+'")
elif p >= 70:
    print("Grade : 'A'")    
elif p >= 60:
    print("Grade : 'B+'")
elif p >= 55:
    print("Grade : 'B'")
elif p >= 50:
    print("Grade : 'C'")
elif p < 50:
    print("Fail..")
else:
    print("Invalid..")
