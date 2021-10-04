r=int(input('enter number of rows:'))
for i in range(r):
    for j in range(i):
        print(' ',end='')
    for j in range(r-i):
        print('* ',end='')
    print()