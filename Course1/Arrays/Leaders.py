#code
T=int(input())
while(T):
    N=int(input())
    O=[]
    A=[int(i) for i in input().split()]
    maxval=0
    for i in range(N-1,-1,-1):
        if(A[i]>=maxval):
            O.append(A[i])
        maxval=max(maxval,A[i])
    for i in range(len(O)-1,-1,-1):
        print(O[i],end=" ")
    print()
    T-=1
    
            
    
