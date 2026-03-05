enrolling_cause = input("Do you want to enroll? (Y/N):").strip().upper()

if enrolling_cause == 'Y' :
    print("Enter the following :")
age = int(input("Enter your age: "))
if age >= 10 and age <= 20:
    print("You are enrolled")
else:
    print("Sorry your age is more than required ." "You can't enroll.")

