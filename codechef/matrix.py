for T in range(int(input())):
    n=int(input())
    lst=[]
    for j in range(n):
        lst1=[int(i) for i in input().split()]
        lst.append(lst1)
    s=0
    s1=0
    s2=0
    for i in range(n):
        s+=lst[i][i]
    for i in range(1,n):
        s1=0
        s2=0
        for j in range(n-i):
            s1+=lst[j+i][j]
            s2+=lst[j][j+i]
        if s1>s:
            s=s1
        if s2>s:
            s=s2
    print(s)
