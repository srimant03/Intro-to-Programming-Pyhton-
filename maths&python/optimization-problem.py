c = float(input("Enter initial price of the car:"))
r = float(input("Enter depreciation rate:"))
mc = 0
x = 50
co = c
for i in range(1,16):
    if i <=5:
        mc = mc + 0.01*c
    else:
        mc = mc + (0.5*mc)
    d = (r/100)*c
    co = co - (d + mc)
    x = x + x*0.1
    v = 6000*(x)
    if v > co:
        break
if v>co:
    print(i)
else:
    print("After 15 years")
     

        

