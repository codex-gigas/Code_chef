n=int(raw_input())
t=0
for test in range(1,n+1):
    a,b=map(int,raw_input().split(" "))
    lst=[x for x in raw_input().split(" ")]
    for item in lst:
        g=int(b)+int(item)
        if (g%7)==0:
            t+=1
    print(t)

       
       
    
