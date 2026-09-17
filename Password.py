passw=input("Set a Password: ")
for l in range(3):
    enter=input("Enter Password: ")
    if passw==enter:

        # Add which comands you want to run under this password
        print("Done!")

        break
    else:
            print("Wrong Password!")
            print("Try Again")