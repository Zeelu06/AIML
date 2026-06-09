secret_value = 47
useratmp = 0

while True:
    userinp = input("Guess a number OR type quit : ")

    if userinp == "quit":
        print("Game over")
        break

    userinp = int(userinp)
    useratmp = useratmp + 1

    if userinp == secret_value :
        print("Win")
        print("Attempts :",useratmp)
        break
        
    elif userinp > 50:
        print("Guess Too High")
        print("Attempts :",useratmp)
    
    else:
        print("Guess Too Low")
        print("Attempts :",useratmp)
