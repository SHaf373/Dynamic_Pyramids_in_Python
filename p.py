r = int(input("Enter Number of Rows : "))
for i in range(r+1):
    for j in range(1,r-i+1):
        print(" ",end='')
    for p in range(1,2*i):
        print("*",end='')
    print()