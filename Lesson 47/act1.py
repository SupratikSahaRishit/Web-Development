#Take input of a word 
string = input("Please enter your own word :")
#Take input of a character 
char = input("Please enter your own character :")
i = 0
count = 0 
#Loop will to find the occurance of character 
while (i < len(string)): #String operation 

    if(string[i] == char ): #Condition 1
        count = count + 1
    i = i + 1


#Display the result 

print("The total number of Times" , char , " has occured = " , count)   
