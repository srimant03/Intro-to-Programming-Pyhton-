class Person:
    def __init__(self):
        self.l1=[]
    def add_obj(self,firstname,lastname,age):
        l=[]
        l.append(firstname)
        l.append(lastname)
        l.append(age)
        self.l1.append(l)
    def obj_info(self):
        return self.l1
    def sort_attribute(self,l1,j):
        def sort2(x):
            return x[j]
        l1.sort(key=sort2)
        return l1

while True:
    print("Welcome to the application!")
    n=int(input("Number of people to be enrolled:"))
    k=int(input("Enter number of queries:"))
    p=Person()
    for i in range(1,n+1):
        l=[str(i) for i in input("Enter space seperated input for first name,last name,age:").split()]
        firstname=l[0]
        lastname=l[1]
        age=l[2]
        p.add_obj(firstname,lastname,age)
    l1=p.obj_info()
    print(p.obj_info())
    for i in range(1,k+1):
        q1=str(input("Enter query:"))
        if q1=="firstname":
            j=0
            l1=p.sort_attribute(l1,j)
        elif q1=="lastname":
            j=1
            l1=p.sort_attribute(l1,j)
        elif q1=="age":
            j=2
            l1=p.sort_attribute(l1,j)
        for i in l1:
            print(*i)
    print("Thanks for using the application,if you wish to restart, press Y, else press N")
    x=str(input("Yes/No?"))
    if x=="Y":
        pass 
    else:
        quit()






    


    
