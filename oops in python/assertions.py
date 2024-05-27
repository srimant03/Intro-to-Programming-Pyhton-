import math 
def mat_mul(A,B):
    l=[]
    for i in range(0,len(A)):
        l1=[]
        for j in range(0,len(B[0])):
            x1=0
            for k in range(0,len(B)):
                x=A[i][k]*B[k][j]
                x1=x1+x
                x1=round(x1,2)
            l1.append(x1)
        l.append(l1)
    return l

def scale(x,y,z,sx,sy,sz,n):
    s=[[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]]
    d=[x,y,z,[1 for i in range(1,n+1)]]
    l=mat_mul(s,d)
    return l

def translate(x,y,z,tx,ty,tz,n):
    t=[[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]]
    d=[x,y,z,[1 for i in range(1,n+1)]]
    l=mat_mul(t,d)
    return l

def rotation(x,y,z,axis,phi,n):
    c=math.cos(math.radians(phi))
    s=math.sin(math.radians(phi))
    if axis=="x":
        r=[[1,0,0,0],[0,c,-1*s,0],[0,s,c,0],[0,0,0,1]]
        d=[x,y,z,[1 for i in range(1,n+1)]]
        l=mat_mul(r,d)
        return l
    if axis=="y":
        r=[[c,0,s,0],[0,1,0,0],[-1*s,0,c,0],[0,0,0,1]]
        d=[x,y,z,[1 for i in range(1,n+1)]]
        l=mat_mul(r,d)
        return l
    if axis=="z":
        r=[[c,-1*s,0,0],[s,c,0,0],[0,0,1,0],[0,0,0,1]]
        d=[x,y,z,[1 for i in range(1,n+1)]]
        l=mat_mul(r,d)
        return l
def test_matmul(A,B,true_C):
    l=mat_mul(A,B)
    try:
        assert l==true_C
    except:
        print("False")
    if l==true_C:
        return True

def test_scale(x, y, z, sx, sy, sz, true_x, true_y, true_z):
    l=scale(x,y,z,sx,sy,sz,n)
    try:
        assert l[0]==true_x
        assert l[1]==true_y 
        assert l[2]==true_z
    except:
        print("False") 
    if l[0]==true_x and l[1]==true_y and l[2]==true_z:
        return True
    
def test_translate(x, y, z, tx, ty, tz, true_x, true_y, true_z):
    l=translate(x,y,z,tx,ty,tz,n)
    try:
        assert l[0]==true_x
        assert l[1]==true_y 
        assert l[2]==true_z 
    except:
        print("False")
    if l[0]==true_x and l[1]==true_y and l[2]==true_z:
        return True

def test_rotate(x, y, z,axis,phi,true_x, true_y, true_z):
    l=rotation(x,y,z,axis,phi,n)
    try:
        assert l[0]==true_x 
        assert l[1]==true_y 
        assert l[2]==true_z
    except:
        print("False")
    if l[0]==true_x and l[1]==true_y and l[2]==true_z:
        return True

for i in range(1,5):
    if i==1:
        n=8
        sx=0.5
        sy=2
        sz=3
        x=[0,0,0,0,4,4,4,4]
        y=[0,0,3,3,3,0,0,3]
        z=[0,2,2,0,0,0,2,2]
        true_x=[0,0,0,0,2,2,2,2]
        true_y=[0,0,6,6,6,0,0,6]
        true_z=[0,6,6,0,0,0,6,6]
    elif i==2:
        n=3
        sx=0.5
        sy=2
        sz=3
        x=[4,0,4]
        y=[0,3,3]
        z=[0,2,2]
        true_x=[2,0,2]
        true_y=[0,6,6]
        true_z=[0,6,6]
    elif i==3:
        n=4
        sx=2
        sy=2
        sz=2
        x=[1,0,1,0]
        y=[4,4,4,4]
        z=[2,3,3,2]
        true_x=[2,0,2,0]
        true_y=[8,8,8,8]
        true_z=[4,6,6,4]
    elif i==4:
        n=8
        sx=0.5
        sy=2
        sz=3
        x=[0,0,0,0,4,4,4,4]
        y=[0,0,3,3,3,0,0,3]
        z=[0,2,2,0,0,0,2,2]
        true_x=[0,0,0,0,2,2,2,2]
        true_y=[0,0,6,6,6,0,0,6]
        true_z=[0,6,6,0,0,0,6,6]
    l=scale(x,y,z,sx,sy,sz,n)
    correct=(test_scale(x, y, z, sx, sy, sz, true_x, true_y, true_z))
    print(correct)
    if correct:
        print("Scaling is correct")
for i in range(1,4):
    if i==1:
        n=3
        tx=1
        ty=2
        tz=3
        x=[4,0,4]
        y=[0,3,3]
        z=[0,2,2]
        true_x=[5,1,5]
        true_y=[2,5,5]
        true_z=[3,5,5]
    elif i==2:
        n=8
        tx=1.5
        ty=2
        tz=3
        x=[0,0,0,0,4,4,4,4]
        y=[0,0,3,3,3,0,0,3]
        z=[0,2,2,0,0,0,2,2]
        true_x=[1.5,1.5,1.5,1.5,5.5,5.5,5.5,5.5]
        true_y=[2,2,5,5,5,2,2,5]
        true_z=[3,5,5,3,3,3,5,5]
    elif i==3:
        n=4
        tx=2
        ty=2
        tz=2
        x=[1,0,1,0]
        y=[4,4,4,4]
        z=[2,3,3,2]
        true_x=[3,2,3,2]
        true_y=[6,6,6,6]
        true_z=[4,5,5,4]
    l=translate(x,y,z,tx,ty,tz,n)
    correct=test_translate(x, y, z, tx, ty, tz, true_x, true_y, true_z)
    print(correct)
    if correct:
        print("Translation is correct")
for i in range(1,4):
    ax=str(input("Enter axis of rotation:"))
    axis=ax
    phi=90
    c=math.cos(math.radians(phi))
    s=math.sin(math.radians(phi))
    x=[0,0,0,0,4,4,4,4]
    y=[0,0,3,3,3,0,0,3]
    z=[0,2,2,0,0,0,2,2]
    n=8
    if ax=="x":
        true_x=[0,0,0,0,4,4,4,4]
        true_y=[0,-2,-2,0,0,0,-2,-2]
        true_z=[0,0,3,3,3,0,0,3]
    if ax=="y":
        true_x=[0,2,2,0,0,0,2,2]
        true_y=[0,0,3,3,3,0,0,3]
        true_z=[0,0,0,0,-4,-4,-4,-4]
    if ax=="z":
        true_x=[0,0,-3,-3,-3,0,0,-3]
        true_y=[0,0,0,0,4,4,4,4]
        true_z=[0,2,2,0,0,0,2,2]
    l=rotation(x,y,z,axis,phi,n)
    correct=test_rotate(x, y, z,axis,phi,true_x, true_y, true_z)
    print(correct)
    if correct:
        print("Rotation is correct")
for i in range(1,6):
    if i==1:
        A=[[1,2,3],[3,2,1],[2,1,3]]
        B=[[0,0,0,0,4,4,4,4],[0,0,3,3,3,0,0,3],[0,2,2,0,0,0,2,2]]
        true_C=[[0,6,12,6,10,4,10,16],[0,2,8,6,18,12,14,20],[0,6,9,3,11,8,14,17]]
    elif i==2:
        A=[[1,-2,1],[2,1,3]]
        B=[[2,1],[3,2],[1,1]]
        true_C=[[-3,-2],[10,7]]
    elif i==3:
        A=[[1,2],[3,4]]
        B=[[5,6,7],[8,9,10]]
        true_C=[[21,24,27],[47,54,61]]
    elif i==4:
        A=[[2,1,4],[0,1,1]]
        B=[[6,3,-1,0],[1,1,0,4],[-2,5,0,2]]
        true_C=[[5,27,-2,12],[-1,6,0,6]]
    elif i==5:
        A=[[-2,1],[0,4]]
        B=[[6,5],[-7,1]]
        true_C=[[-19,-9],[-28,4]]
    l=mat_mul(A,B)
    correct=test_matmul(A,B,true_C)
    print(correct)
    if correct:
        print("Matrix Multiplication is Correct!")





    











        
            
