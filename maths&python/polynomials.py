n = int(input("Degree of polynomial:"))
if n == 3:
    a = float(input("Enter first coeff:"))
    b = float(input("Enter second coeff:"))
    c = float(input("Enter third coeff:"))
    d = float(input("Enter fourth coeff:"))
elif n == 2:
    a = float(input("Enter first coeff:"))
    b = float(input("Enter second coeff:"))
    c = float(input("Enter third coeff:"))
elif n == 1:
    a = float(input("Enter first coeff:"))
    b = float(input("Enter second coeff:"))
else:
    print("ERROR:WrongInput")
l = float(input("Enter Lower bound for x:"))
u = float(input("Enter upper bound for x:"))
s = float(input("Enter the steps in which you wish to increment x:"))
if n == 3:
    x = l
    while x<=u:
        f1 = a*x*x*x + b*x*x + c*x + d
        v = round(f1)
        if v<0:
            print("*"*0)
        if v>=0:
            print("*"*v)
        x = x+s
if n == 2:
    x = l
    while x<=u:
        f1 = a*x*x + b*x + c 
        v = round(f1)
        if v<0:
            print("*"*0)
        if v>=0:
            print("*"*v)
        x = x + s
if n == 1:
    x = l
    while x<=u:
        f1 = a*x + b 
        v = round(f1)
        if v<0:
            print("*"*0)
        if v>=0:
            print("*"*v)
        x = x + s
















    

    