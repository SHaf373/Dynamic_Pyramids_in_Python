r=int(input('enter number of rows:'))
for i in range(r):
    for j in range(r-i-1):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()
