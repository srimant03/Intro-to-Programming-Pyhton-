a = float(input("Enter lower limit:"))
b = float(input("Enter upper limit:"))
d = float(input("Enter common difference:"))
l = [2,1]
if (b-a)%d != 0:
        exit()
def calculate_area(a,b,d,l):
    def func(a):
        f = 0
        for i in l:
            f = f + a**i
        return f
    x = 0
    f=0
    n = (b-a)/d
    n = int(n)
    for i in range(1,(n+1)):
        x1 = ((a+d - a)/6)
        f1 = func(a)
        f2 = func((a+(a+d))/2)
        f3 = func(a+d)
        x = x1*(f1+(4*f2)+f3)
        f = f+x
        a = a+d
    print(f)
calculate_area(a,b,d,l)



