#take input 
print("Half Pyramid Pattern of Stars (*):")
n = int(input("enter the number of rows :"))
#Outer loop to handle the number of rows
for i in range (n):
    #Inner loop to handle the number of columns 
    for j in range (i+1):
        #display result 
        print("*" , end = "")
        print()
    