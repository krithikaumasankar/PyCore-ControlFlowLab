t = input("Enter the temperature (warm/cold): ")
h = input("Enter the humidity (dry/humid): ")
if t == "warm":
    if h == "dry":
        print("Play Basketball")
    elif h == "humid":
        print("Play Tennis")
    else: 
        print("Invalid input")
elif t == "cold":
    if h == "dry":
        print("Play cricket")
    elif h == "humid":
        print("Swim")
    else:
        print("Invalid input..")
else:
    print("Invalid input")
