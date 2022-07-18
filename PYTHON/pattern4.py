n=int(input('Enter the limit : '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<=n-i):
            print('',end="_")
        else:
            print('*',end=" ")
    print()