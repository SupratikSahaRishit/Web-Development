#Input a number 
num = int(input("Enter the number:"))
t = num 
numLen = 0 
#iterate the loop
while t>0:
    numLen = numLen + 1
    t = int(t/10)
     
if numLen>= 4: #Condition 1 
    numLen = int(numLen/2)
    chk = 0
    while num>0: #iterate loop
        rem = num%10
    if chk == numLen: #nested condition 1 
        midOne = rem 
    elif chk==(numLen-1):
        midTwo = rem
    num = int(num/10)
    chk = chk + 1
    prod = midOne + midTwo #Product of middle digits 

    #Dispaly the result 

print("\n Product od Mid digits"()")


