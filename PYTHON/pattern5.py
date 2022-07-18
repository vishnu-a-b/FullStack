n=int(input('Enter the limit : '))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if(j>=i+1):
            print('',end=" ")
        else:
            print('*',end=" ")
    print()