valid = False
while not valid: 
    try:
        age=int(input("Enter the age "))


        while age>18:

            print("You are eligible to vote ")
        valid = True
    except ValueError:
        print("Invalid")

        