r = int(input("Enter Number of Rows : "))
for i in range(r+1):
    for j in range(r-i+1):
        print(" ",end='')
    for j in range(1,2*i):
        print("*",end='')
    print()
for i in range(r-1, 0, -1):
    for j in range(r-i+1):
        print(" ",end='')
    for j in range(1,2*i):
        print("*",end='')
    print()