def decimal_binary(n):
    n=int(n)
    l=[]
    while n!=0:
        i=n%2
        n=n//2
        l.append(i)
    l=l[::-1]
    return l

def decimal_hex(n):
    n=int(n)
    l=[]
    while n!=0:
        i=n%16
        n=n//16
        if i==10:
            i= "A"
        elif i==11:
            i="B"
        elif i==12:
            i="C"
        elif i==13:
            i="D"
        elif i==14:
            i="E"
        elif i==15:
            i="F"
        else:
            i=i
        l.append(i)
    l=l[::-1]
    return l
def dec_oct(n):
    n=int(n)
    l=[]
    while n!=0:
        i=n%8
        n=n//8
        l.append(i)
    l=l[::-1]
    return l
def bin_dec(s):
    str(s)
    s=s[::-1]
    sum=0
    n=0
    for i in s:
        i=int(i)
        y=i*(2**n)
        sum=sum+y
        n=n+1
    return sum

def bin_oct(n):
    y=bin_dec(n)
    a=dec_oct(y)
    return a

def bin_hex(n):
    y=bin_dec(n)
    a=decimal_hex(y)
    return a

def hex_dec(s):
    str(s)
    s=s[::-1]
    sum=0
    n=0
    for i in s:
        if i=="A":
            i=10
        if i=="B":
            i=11
        if i=="C":
            i=12
        if i=="D":
            i=13
        if i=="E":
            i=14
        if i=="F":
            i=15
        else:
            i=int(i)
        y=i*(16**n)
        sum=sum+y
        n=n+1
    return sum

def hex_bin(s):
    y=hex_dec(s)
    z=decimal_binary(y)
    return z

def hex_oct(s):
    y=hex_dec(s)
    z=dec_oct(y)
    return z

def oct_dec(s):
    str(s)
    s=s[::-1]
    sum=0
    n=0
    for i in s:
        i=int(i)
        y=i*(8**n)
        sum=sum+y
        n=n+1
    return sum

def oct_hex(s):
    y=oct_dec(s)
    z=decimal_hex(y)
    return z
def oct_bin(s):
    y=oct_dec(s)
    z=decimal_binary(y)
    return z

def valid(x,y):
    l=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    c=1
    for i in x:
        if i not in l[0:y]:
            c=0
    return c

def A_B():
    a=int(input("Enter initial radix:"))
    b=int(input("Enter final radix:"))
    s=str(input("Enter number:"))
    z=valid(s,a)
    if z==0:
        q=0
        return q
    else:
        def assign1(x):
            if (x)>= '0' and (x) <= '9':
                return ord(x) - ord('0')
            else:
                return ord(x) - ord('A') + 10
        def assign2(x):
            if (x >= 0 and x <= 9):
                return chr(x + ord('0'))
            else:
                return chr(x - 10 + ord('A'))
        sum=0
        n=(len(s)-1)
        for i in s:
            i=assign1((i))
            y= i*(a**(n))
            n=n-1
            sum=sum+y
        sum=int(sum)
        l=[]
        while sum!=0:
            i=sum%b
            sum=sum//b
            i=assign2(i)
            l.append(i)
        l=l[::-1]
        return l
while 1>0:
    print("Select an operation:")
    print("1.Convert decimal to binary.")
    print("2.Convert decimal to hexadecimal.")
    print("3.Convert decimal to octal.")
    print("4.Convert binary to hexadecimal.")
    print("5.Convert binary to octal.")
    print("6.Convert binary to decimal.")
    print("7.Convert hexadecimal to binary")
    print("8.Convert hexadecimal to decimal")
    print("9.Convert hexadecimal to octal")
    print("10.Convert octal to binary")
    print("11.Convert octal to decimal")
    print("12.Convert octal to hexadecimal")
    print("13.Convert number with radix A to radix B.")
    print("14.Exit")
    n=int(input())
    if n==1:
        s=str(input("Enter decimal no.:"))
        z=valid(s,10)
        if z==0:
            print("Wrong input")
        else:
            l=decimal_binary(s)
            print(*l,end="")
    elif n==2:
        s=str(input("Enter decimal no.:"))
        z=valid(s,10)
        if z==0:
            print("Wrong input")
        else:
            l=decimal_hex(s)
            print(*l,end="")
    elif n==3:
        s=str(input("Enter decimal no.:"))
        z=valid(s,10)
        if z==0:
            print("Wrong input")
        else:
            l=dec_oct(s)
            print(*l,end="")
    elif n==4:
        s=str(input("Enter binary no.:"))
        z=valid(s,2)
        if z==0:
            print("Wrong Input")
        else:
            l=bin_hex(s)
            print(*l,end="")
    elif n==5:
        s=str(input("Enter binary no.:"))
        z=valid(s,2)
        if z==0:
            print("Wrong Input")
        else:
            l=bin_oct(s)
            print(*l,end="")
    elif n==6:
        s=str(input("Enter binary no.:"))
        z=valid(s,2)
        if z==0:
            print("Wrong Input")
        else:
            l=bin_dec(s)
            print(l)
    elif n==7:
        s=str(input("Enter hexadecimal no.:"))
        z=valid(s,16)
        if z==0:
            print("Wrong Input")
        else:
            l=hex_bin(s)
            print(*l,end="")
    elif n==8:
        s=str(input("Enter hexadecimal no.:"))
        z=valid(s,16)
        if z==0:
            print("Wrong Input")
        else:
            l=hex_dec(s)
            print(l)
    elif n==9:
        s=str(input("Enter hexadecimal no.:"))
        z=valid(s,16)
        if z==0:
            print("Wrong Input")
        else:
            l=hex_oct(s)
            print(*l,end="")
    elif n==10:
        s=str(input("Enter octal no.:"))
        z=valid(s,8)
        if z==0:
            print("Wrong Input")
        else:
            l=oct_bin(s)
            print(*l,end="")
    elif n==11:
        s=str(input("Enter octal no.:"))
        z=valid(s,8)
        if z==0:
            print("Wrong Input")
        else:
            l=oct_dec(s)
            print(l)
    elif n==12:
        s=str(input("Enter octal no.:"))
        z=valid(s,8)
        if z==0:
            print("Wrong Input")
        else:
            l=oct_hex(s)
            print(*l,end="")
    elif n==13:
        l=A_B()
        if l==0:
            print("wrong input")
        else:
            print(*l,end="")
    elif n==14:
        quit()
    print("\n")













        








        




        
        












            


        





