#code
T=int(input())
while(T>0):
    N=int(input())
    val=-1
    
    flag=0
    A=[int(n) for n in input().split()]
    if(N==1):
        flag=1
        print(A[0])
    elif(N==2):
        flag=1
        print(val)
    else:
        x=0
        for i in A:
            right=A[0:x]
            left=A[x+1:]
            if(sum(left)==sum(right)):
                flag=1
                print(A[x])
        x+=1
    if(flag==0):
        print(val)
    print()
    T-=1
