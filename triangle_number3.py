r=int(input('enter number of rows:'))
num=1
for i in range(r):
    for j in range(i+1):
        print(num,end='')
        num+=1
    print()