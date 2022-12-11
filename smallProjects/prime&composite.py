print("Welcome to Check Prime or composite number given by you")

def checkPC():
    num = int(input("Enter Any number You want to check:- "))

    if num % 2 != 0:
        print("This is prime number!!")
    else:
        print("This is Composite Number!!")
    print("--------------------------------------------------------------------------")
    again = input("Enter n for check again:- ")
    if again == "y":
        checkPC()
    else:
        print("The porgram was stopped! \nThank you to give me Change to serve You!")

checkPC()