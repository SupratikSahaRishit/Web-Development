#Take two input from the user 
lower = int(input("enter a upper range :"))
upper = int(input("enter a lower range :"))


print("Prime numbers between " , lower , "and" , upper , "are:")
#Literate loop from lower limit to upper limit 
for num in range(lower , upper + 1):
    #All prime numbers are greater than 1 
    if num > 1 :
        for i in range(2 , num ):
            if (num % i) == 0 :
              break
        else:
            print(num)
