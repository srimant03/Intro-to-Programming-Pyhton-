from datetime import datetime
class BankAccount:
    def __init__(self,username,password,balance):
        self.un=username
        self.pw=password
        self.bal=balance
    def authenticate(self):
        self.sp=str(input("Enter secret password:"))
        if self.sp==self.pw:
            return True
        else:
            return False
    def deposit(self,d):
        c=0
        while c<=2:
            x=BankAccount.authenticate(self)
            if x:
                global dt
                dt=dt+d
                self.bal=self.bal+dt-wt
                l=[]
                x=datetime.now()
                x=str(x)
                l.append(x)
                y="The amount of Rs."+str(d)+" has been added.Current balance is Rs."+str(self.bal)
                l.append(y)
                self.f=open(self.un+".txt","a")
                self.f.writelines(l)
                self.f.write("\n")
                self.f.close()
                break
            else:
                c=c+1
                try:
                    assert c<=2
                except:
                    print("Too many wrong attempts")
    def withdraw(self,w):
        c=0
        while c<=2:
            x=BankAccount.authenticate(self)
            if x:
                if self.bal<w:
                    print("Low balance!! Cannot be debited at this time!")
                    break
                else:
                    global wt
                    wt=wt+w
                    self.bal=self.bal+dt-wt
                    l=[]
                    x=datetime.now()
                    x=str(x)
                    l.append(x)
                    l.append("The amount of Rs."+str(w)+"has been debited. Current balance is"+str(self.bal))
                    self.f=open(self.un+".txt","a")
                    self.f.writelines(l)
                    self.f.write("\n")
                    self.f.close()
                    break
            else:
                c=c+1
                try:
                    assert c<=2
                except:
                    print("Too many wrong attempts")
    def bankstatement(self):
        c=0
        while c<=2:
            x=BankAccount.authenticate(self)
            if x:
                self.f=open(self.un+".txt","r")
                l1=self.f.readlines()
                for line in l1:
                    print(line)
                break
            else:
                c=c+1
                try:
                    assert c<=2
                except:
                    print("Too many wrong attempts")

print("Welcome to Bank of IIITD")
print("")
username=str(input("Enter your username:"))
password=str(input("Enter your password:"))
balance=float(input("Enter starting balnce for your account:"))
dt=0
wt=0
while True:
    print("-"*25,"MENU","-"*25)
    print("1.Select to deposit amount")
    print("2.Select to withdraw amount")
    print("3.Select to get bank statement")
    n=int(input("Enter your operation:"))
    b=BankAccount(username,password,balance)
    if n==1:
        d=float(input("Provide amount to be deposited:"))
        b.deposit(d)
    elif n==2:
        w=float(input("Enter amount to be withdrawn:"))
        b.withdraw(w)
    elif n==3:
        b.bankstatement()
    cont=str(input("Do you wish to continue?(Y/N)"))
    if cont=="Y":
        pass
    elif cont=="N":
        break






