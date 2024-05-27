n=int(input("Enter size of 2D matrix:"))
l=[]
for i in range(1,n+1):
    l1=[str(j) for j in input("Enter all elements of row "+ str(i)+":").split()]
    l.append(l1)
for i in range(len(l)):
    print(*l[i])
while True:
    print("\n")
    print("Choose an operation:")
    print("1.Normal traversal")
    print("2.Alternating traversal")
    print("3.Spiral traversal from outer to inwards")
    print("4.Boundary traversal")
    print("5.Diagonal traversal from right to left")
    print("6.Diagonal traversal from left to right")
    print("7.Exit")

    n1=int(input("Enter operation number:"))
    if n1==1:
        for i in range(0,len(l)):
            print(*l[i],end=" ")
    if n1==2:
        for i in range(0,len(l)):
            if i%2==1:
                l[i]=l[i][::-1]
                print(*l[i],end=" ")
            else:
                print(*l[i],end=" ")
    if n1==3:
        if n%2==0:
            x=0
            y=n
            while y-x!=0:
                for i in range(x,y):
                    print(l[x][i],end=" ")
                for i in range(x+1,y-1):
                    print(l[i][y-1],end=" ")
                for i in range(y-1,x-1,-1):
                    print(l[y-1][i],end=" ")
                for j in range(y-2,x,-1):
                    print(l[j][x],end=" ")
                x=x+1
                y=y-1
        if n%2==1:
            x=0
            y=n
            while y-x!=1:
                for i in range(x,y):
                    print(l[x][i],end=" ")
                for i in range(x+1,y-1):
                    print(l[i][y-1],end=" ")
                for i in range(y-1,x-1,-1):
                    print(l[y-1][i],end=" ")
                for j in range(y-2,x,-1):
                    print(l[j][x],end=" ")
                x=x+1
                y=y-1
            a=int((n-1)/2)
            print(l[a][a])
    if n1==4:
        print(*l[0],end=" ")
        for i in range(1,n-1):
            print(l[i][-1],end=" ")
        l2=l[n-1][::-1]
        print(*l2,end=" ")
        for j in range(n-2,0,-1):
            print(l[j][0],end=" ")
    if n1==5:
        x=0
        while x<=n-1:
            j=x
            for i in range(0,x+1):
                print(l[i][j],end=" ")
                j=j-1
            x=x+1
        x=1
        while x<=n-1:
            j=n-1
            for i in range(x,n):
                print(l[i][j],end=" ")
                j=j-1
            x=x+1
    if n1==6:
        x=n-1
        while x>=0:
            i=0
            for j in range(x,n):
                print(l[i][j],end=" ")
                i=i+1
            x=x-1
        x=1
        while x<=n-1:
            j=0
            for i in range(x,n):
                print(l[i][j],end=" ")
                j=j+1
            x=x+1
    if n1==7:
        exit()


    




