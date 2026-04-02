rows = int(input("Please Enter the Total Number of Rows : "))
ch = '*'

print("Mirrored Right Triangle Pattern")
for i in range(1, rows + 1):
    # Print spaces
    for j in range(1, rows - i + 1):
        print(' ', end=' ')
    
    # Print characters
    for k in range(1, i + 1):
        print(ch, end=' ')
        
    print()