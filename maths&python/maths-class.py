n = int(input("Enter number of students:"))    
for i in range(1,n+1):                         #loop will be executed 'n' times depending on n.
    d = str(input("Enter shape dimension:"))   #Entering 2D will give list of all 2D shapes and 3D will give a list of 3D shapes.
    if d == "2D":
        l = ["1.Square","2.Rectangle","3.Rhombus","4.Parallelogram","5.Circle","13.Exit"]
        print("-"*5, "MENU", "-"*5)
        print("2D Shapes are:")
        print(*l, sep = "\n")         #print all 2D shapes from the list, each in a new line.

        c = str(input("Choose a 2D shape(Enter shape code):"))
        if c == "1":
            print("You chose square")
            s = float(input("Enter side of square:"))
            print("Perimeter of the square is:", 4*s)
            print("Area of the square is:", s*s)
        elif c == "2":
            print("You chose rectangle")
            l = float(input("Enter length of rectangle:"))
            b = float(input("Enter breadth of rectangle:"))
            print("Perimeter of the rectangle is:", 2*(l+b))
            print("Area of the rectangle is:", l*b)
        elif c == "3":
            print("You chose rhombus")
            a = float(input("Enter side of rhombus:"))
            d1 = float(input("Enter diagonal:"))
            d2 = float(input("Enter diagonal:"))
            print("Perimeter of the rhombus is:", 4*a)
            print("Area of the rhombus is:", (1/2)*d1*d2)
        elif c == "4":
            print("You chose parallelogram")
            l = float(input("Enter length of the parallelogram:"))
            b = float(input("Enter base of the parallelogram:"))
            h = float(input("Enter height of the parallelogram:"))
            #by convention height is measured from base and same is used for area calculation
            print("Perimeter of the parallelogram is:", 2*(l+b))
            print("Area of the parallelogram is:", b*h)
        elif c == "5":
            print("You chose circle")
            r = float(input("Enter radius of the circle:"))
            print("Perimeter of circle is:", 2*3.14*r)
            print("Area of the circle is:", 3.14*r*r)
        elif c == "13":
            break
        else:
            print("ERROR: WrongInput")
    elif d == "3D":
        l = ["6.Cube", "7.Cuboid", "8.Right Circular Cone", "9.Hemisphere", "10.Sphere", "11.Solid Cylinder", "12.Hollow Cylinder","13.Exit"]
        print("-"*5, "MENU", "-"*5)
        print("3D Shapes are:")
        print(*l, sep = "\n")    #print all 3D shapes from the list, each in a new line
        c = str(input("Choose a 3D shape(Enter shape code):"))
        if c == "6":
            print("You chose cube")
            s = float(input("Enter side of the cube:"))
            print("CSA of the cube is:", 4*s*s)
            print("TSA of the cube is:", 6*s*s)
            print("Volume of the cube is:", s*s*s)
        elif c == "7":
            print("You chose cuboid")
            l = float(input("Enter length of the cuboid:"))
            b = float(input("Enter breadth of the cuboid:"))
            h = float(input("Enter height of the cuboid:"))
            print("CSA of the cuboid is:", 2*(l+b)*h)
            print("TSA of the cuboid is:", 2*(l*b + l*h + b*h))
            print("Volume of the cuboid is:", l*b*h)
        elif c == "8":
            print("You chose right circular cone")
            l = float(input("Enter slant height of the cone:"))
            r = float(input("Enter radius of the cone:"))
            h = float(input("Enter height of the cone:"))
            print("CSA of the cone is:", 3.14*r*l)
            print("TSA of the cone is:", 3.14*r*(r+l))
            print("Volume of the cone is:", (1/3)*3.14*h*(r**2))
        elif c == "9":
            print("You chose hemisphere")
            r = float(input("Enter radius of hemisphere:"))
            print("CSA of the hemisphere is:", 2*3.14*r*r)
            print("TSA of the hemisphere is:", 3*3.14*r*r)
            print("Volume of the hemisphere is:", (2/3)*3.14*(r**3))
        elif c == "10":
            print("You chose sphere")
            r = float(input("Enter radius of sphere:"))
            print("CSA of the sphere is:", 4*3.14*r*r)
            print("TSA of the sphere is:", 4*3.14*r*r)
            print("Volume of the sphere is:", (4/3)*3.14*(r**3))
        elif c == "11":
            print("You chose solid cylinder")
            r = float(input("Enter radius of the solid cylinder:"))
            h = float(input("Enter height of the solid cylinder:"))
            print("CSA of the solid cylinder is:", 2*3.14*r*h)
            print("TSA of the solid cylinder:", 2*3.14*r*(r+h))
            print("Volume of the solid cylinder is:", 3.14*r*r*h )
        elif c == "12":
            print("You chose hollow cylinder")
            r1 = float(input("Enter inner radius of the hollow cylinder:"))
            r2 = float(input("Enter outer radius of the hollow cylinder:"))
            h = float(input("Enter height of the hollow cylinder:"))
            print("CSA of the hollow cylinder is:", 2*3.14*(r1+r2)*h)
            print("TSA of the hollow cylinder:", (2*3.14*(r1+r2)*h + 2*3.14*((r2**2)-(r1**2))))
            print("Volume of the hollow cylinder is:", 3.14*((r2**2) - (r1**2))*h )
        elif c == "13":
            break
        else:
            print("ERROR: WrongInput")
    else:
        print("ERROR: WrongInput")

        
    
        


        
            
            



            
        






    









    
       
        


            
        
            


    



