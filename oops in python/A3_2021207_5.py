class Company:
    def __init__(self,cname,requiredcgpa,branches,positionsOpen):
        self.cname=cname
        self.rcgpa=requiredcgpa
        self.branches=branches
        self.posOpen=positionsOpen
        self.appliedStudents=[]
        self.appOpen=True
    def hireStudents(self):
        self.appliedStudents.sort(key=lambda x:x.cgpa,reverse=True)
        l=[]
        k=self.posOpen
        if k<len(self.appliedStudents): 
            for i in range(0,k):
                l.append(self.appliedStudents[i].name)
                self.appliedStudents[i].isPlaced=True
            return l
        else:
            for i in range(0,len(self.appliedStudents)):
                l.append(self.appliedStudents[i].name)
                self.appliedStudents[i].isPlaced=True
            return l
    def closeApplication(self):
        self.appOpen=False 
        return "The company hired "+len(self.l)+" students"
class Students:
    def __init__(self,name,cgpa,branch):
        self.name=name
        self.cgpa=cgpa
        self.branch=branch 
        self.isPlaced=False 
    def isEligible(self,Company):
        if self.cgpa>=Company.rcgpa and self.branch in Company.branches and self.isPlaced==False:
            return True
        else:
            return False
    def apply(self,i,Company):
        Company.appliedStudents.append(i)
    def getsPlaced(self):
        self.isPlaced=True 
print("Welcome to the placement portal")
n1=int(input("Enter number of students:"))
l1=[]
for j in range(0,n1):
    name=str(input("Enter name of student:"))
    cgpa=float(input("Enter cgpa of student:"))
    try:
        assert cgpa<=10 and cgpa>=0
    except:
        print("The cgpa is invalid")
        cgpa=float(input("Kindly provide correct and valid cgpa:"))
    branch=str(input("Enter branch of student:"))
    s1=Students(name,cgpa,branch)
    l1.append(s1)
n2=int(input("Enter no. of companies:"))
for j in range(1,n2+1):
    cname=str(input("Enter name of company:"))
    requiredcgpa=float(input("Enter required cgpa for Company:"))
    branches=[str(i) for i in input("Enter space seperated branches:").split()]
    positionsOpen=int(input("Enter number of positions open:"))
    c=Company(cname,requiredcgpa,branches,positionsOpen)
    for i in l1:
        if (i.isEligible(c)):
            print("Student "+i.name+" is eligible for "+c.cname)
            i.apply(i,c)
        else:
            print("Student "+i.name+" is not eligible for "+c.cname)
    print("The company "+cname+" hired the following students")
    x=(c.hireStudents())
    for j in x:
        print(j)
    print("The company hired "+str(len(x))+" students")
    





            

                

        








    
    








