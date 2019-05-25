#code
T=int(input())
while(T>0):
    N=int(input())
    A=[int(n) for n in input().split()]
    flag=0
    for i in A:
        c=0
        c=A.count(i)
        if(c>N//2):
            flag=1
            print(i)
            break
    if(flag==0):
        print(-1)
    T-=1
    
    
    
    
    
    
    
    
    
    
    
    
