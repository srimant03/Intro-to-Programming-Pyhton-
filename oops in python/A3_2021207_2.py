class LaundryService:
    def __init__(self,name,contact,email,clothtype,branded,season):
        global id
        self.name=name
        self.cont=contact
        self.email=email
        self.type=clothtype
        self.brand=branded
        self.seas=season
        self.id=id
    def customerDetails(self):
        print("Customer ID:",id)
        print("Customer Name:",self.name)
        print("Contact no.:",self.cont)
        print("Customer email:",self.email)
        print("Type of cloth:",self.type)
        if self.brand==1:
            self.brand=True
        else:
            self.brand=False
        print("Branded or not:",self.brand)
    def calculateCharge(self):
        if self.type=="Cotton":
            self.p=50
        elif self.type=="Silk":
            self.p=30
        elif self.type=="Woolen":
            self.p=90
        elif self.type=="Polyester":
            self.p=20
        if self.brand:
            self.p=1.5*(self.p)
        if self.seas=="Winter":
            self.p=0.5*(self.p)
        else:
            self.p=2*(self.p)
        return self.p
    def findDetails(self):
        l=LaundryService(name,contact,email,clothtype,branded,season)
        l.customerDetails()
        charge=l.calculateCharge()
        print("Total Charge:",charge)
        if charge>200:
            print("To be returned in 4 days!")
        else:
            print("To be returned in 7 days!")

for i in range(1,10):
    id=i
    name=str(input("Enter your name:"))
    contact=int(input("Enter your contact number:"))
    email=str(input("Enter your Email ID:"))
    clothtype=str(input("Enter type of cloth:"))
    branded=int(input("Enter 1 if item is branded, otherwise enter 0:"))
    season=str(input("Enter season:"))
    l=LaundryService(name,contact,email,clothtype,branded,season)
    l.findDetails()






