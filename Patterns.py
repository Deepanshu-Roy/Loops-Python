passw=input("Set a Password: ")
for l in range(3):
    enter=input("Enter Password: ")
    if passw==enter:
        print("Press 1: To Run the pattern")
        print("Press 2: For closing the program")
        con=int(input("Press Either 1/2: "))
        if con==1:
            for i in range(4):
                print("*", end=' ')
                for j in range(i):
                    print("*", end=' ')
                print()

            for a in range(3):
                print("*", end=' ')
                for b in range(4):
                    print("*", end=' ')
                print()

            for k in range(4,0,-1):
                print("*", end=' ')
                for h in range(k):
                    print("*", end=' ')
                print()
        elif con==2:
            print("Program Ended. Thank You!")
        break
    else:
        print("Wrong Password!")
        print("Try Again")