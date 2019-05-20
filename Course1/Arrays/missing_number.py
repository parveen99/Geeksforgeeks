T=int(input())
for _ in range(T):
    N=int(input())
    C=list(map(int,input().split()))
    
    total=N*(N+1)/2
    Sum=sum(C)
    total=total-Sum
    print(int(total))
        
    
