e = [float(i) for i in input("Enter origin vector of light ray:").split()]
e1 = e[0]
e2 = e[1]
e3 = e[2]
d = [float(i) for i in input("Enter direction vector of light ray:").split()]
dx = d[0]
dy = d[1]
dz = d[2]
x0 = float(input("Enter x-coordinate of origin of sphere:"))
y0 = float(input("Enter y-coordinate of origin of sphere:"))
z0 = float(input("Enter z-coordinate of origin of sphere:"))
r = float(input("Enter radius of sphere:"))
for t in range(1,1001):
    x1 = e1 + t*dx 
    y1 = e2 + t*dy 
    z1 = e3 + t*dz
    x2 = e1 + (t+1)*dx
    y2 = e2 + (t+1)*dy
    z2 = e3 + (t+1)*dz
    r1 = (x1-x0)**2 + (y1-y0)**2 + (z1-z0)**2
    r2 = (x2-x0)**2 + (y2-y0)**2 + (z2-z0)**2
    if  (r1 > r**2 and r2 < r**2) or (r1<r**2 and r2>r**2):
        print(x1, y1, z1)
        print(x2,y2,z2)
        print()




    







