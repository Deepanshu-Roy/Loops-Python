print("Press 1: To Run the pattern")
print("Press 2: For closing the program")
con=int(input("Press Either 1/2: "))
if con==1:
    for i in range(5):
        print("*", end=' ')
        for j in range(i):
            print("*", end=' ')
        print()
elif con==2:
    print("Program Ended. Thank You!")