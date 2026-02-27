# INPUT A WORD OR SENTENCE 
string = input("Please enter your own string :")

string2 = ('')
# Loop for printing in reverse 
for i in string:
    string2 = i + string2

print("\n The original string =" , string)
print("\n The reversed string =" , string2)