a = float(input("Price of Item1:"))
b = float(input("Price of Item2:"))
c = float(input("Price of Item3:"))
print("<","-"*50)
print("")
print("-"*50,">")
print("Discount Details")
print("")
d = float(input("Discount(in percentage) for ComboPack1:"))
if d>100 or d<0:
    print("Error")
e = float(input("Discount(in percentage) for ComboPack2:"))
if e>100 or e<0:
    print("Error")
f = float(input("Discount(in percentage) for ComboPack3:"))
if e>100 or e<0:
    print("Error")
print("<","-"*50)
print("")
g = str(input("Enter your 10-Digit contact number:"))
if len(g) != 10:
    print("Error")
print("The resulting catalogue is:")
print("-"*50)
print("")
print("-"*50)
print("Delhi Days")
print("R-Block, Model Town-3")
print("Delhi: 110009")
print("-"*50)
print("")
print("-"*50)
print("Item       Price(per pack)")
print("")
print("Item1     ",a)
print("Item2     ",b)
print("Item3     ",c)
cp1 = (a+b)-((a+b)*(d/100))
cp2 = (a+c)-((a+c)*(e/100))
cp3 = (b+c)-((b+c)*(f/100))
print("ComboPack1",cp1)
print("ComboPack2",cp2)
print("ComboPack3",cp3)
ss = (a+b+c)-((a+b+c)*(28/100))
print("SuperSaver",ss)
print("-"*50)
print("")
print("-"*50)
print("")
print("For home delivery, contact here: 9876543210")











