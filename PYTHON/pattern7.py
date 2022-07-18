st=input('Enter the string : ')
n=len(st)
for i in range(1,n+1):
    for j in range(1,n+1):
        
        if(j==i):
            print(st[j-1],end=" ")
        elif(j==n-i+1):
            print(st[j-1],end=" ")
        elif(j<=n-i and j>i):
            print('',end="  ")
        else:
            print('',end="  ")
        
            
    print()