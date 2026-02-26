# Take input of number of units consumed by the user 
units = int(input("Please enter the number of units consumed :"))
# Check conditions of units consumed 
# Then calculate amount and surcharge accordingly 
# Surcharge is the tax value 

# Check for units less than 50 
if(units < 50):
    amount = units * 2.60
    surcharge = 25

# Check for units less than 100
elif (units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

# Check for units or less than or equal to 200 
elif(units <= 200):
    amount = 130 + 162.50 + ((units) * 5.26)
    subcharge = 55

# Check for all the other cases than mentioned
# When units consumed are more than 200
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

# Calculate and display the total elctricity bill
# Total amount = amount + subcharge
total = amount +subcharge
print ("\nElectricity Bill = %2f" %total)


    