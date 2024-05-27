import math
n=int(input("Enter number of vertices of the 3D-shape:"))
x=[float(i) for i in input("Enter all x-coordinates of vertices:").split()]
y=[float(i) for i in input("Enter all y-coordinates of vertices:").split()]
z=[float(i) for i in input("Enter all z-coordinates of vertices:").split()]
q=int(input("Enter number of transformation queries to be applied:"))
for i in range(1,q+1):
    t=[str(i) for i in input().split()]
    if t[0]=="S":
        x=[float(t[1])*j for j in x]
        y=[float(t[2])*j for j in y]
        z=[float(t[3])*j for j in z]
    if t[0]=="T":
        x=[float(t[1])+j for j in x]
        y=[float(t[2])+j for j in y]
        z=[float(t[3])+j for j in z]
    if t[0]=="R":
        if t[1]=="x":
            c=math.cos(math.radians(float(t[2])))
            s=math.sin(math.radians(float(t[2])))
            xp=x.copy()
            yp=y.copy()
            zp=z.copy()
            for j in range(0,len(x)):
                x[j]=xp[j]
                y[j]=(yp[j]*c)-(zp[j]*s)
                z[j]=(yp[j]*s)+(zp[j]*c)
        if t[1]=="y":
            c=math.cos(math.radians(float(t[2])))
            s=math.sin(math.radians(float(t[2])))
            xp=x.copy()
            yp=y.copy()
            zp=z.copy()
            for j in range(0,len(x)):
                x[j]=(xp[j]*c)+(zp[j]*s)
                y[j]=yp[j]
                z[j]=(zp[j]*c)-(xp[j]*s)
        if t[1]=="z":
            c=math.cos(math.radians(float(t[2])))
            s=math.sin(math.radians(float(t[2])))
            xp=x.copy()
            yp=y.copy()
            zp=z.copy()
            for j in range(0,len(x)):
                x[j]=(xp[j]*c)-(yp[j]*s)
                y[j]=(xp[j]*s)+(yp[j]*c)
                z[j]=zp[j]

print(x)
print(y)
print(z)
l=[]
x1=[]
y1=[]
z1=[]
for i in x:
    i=str(i)
    x1.append(i+",")
l.append(x1)
for i in y:
    i=str(i)
    y1.append(i+",")
l.append(y1)
for i in z:
    i=str(i)
    z1.append(i+",")
l.append(z1)


f=open("coordinates.txt","w")
f.writelines(l[0])
f.write("\n")
f.writelines(l[1])
f.write("\n")
f.writelines(l[2])



        
