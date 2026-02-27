# Input an integer greater than 1
n = int(input("Enter the value of N:"))

# Print the numbers form n to 1
print("Numbers form {0} to {1} are:".format(n,1))

# Loop to print numbers
for i in range (n,0,-1):
    print(i)
