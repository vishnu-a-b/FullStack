n=int(input('Enter the limit : '))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        if(i==n or j==i or j==1):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()