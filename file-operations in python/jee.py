f=open("Admin\\RegisteredStudents.txt","r")
for line in f:
    l=line.split()
    x=l[0]+"_"+l[1]
    y=l[0]+" "+l[1]
    z="Student\\"+x+".txt"
    with open(z,"r") as f1, open("Admin\\AnswerKey.txt","r") as f2:
        l1=[]
        for line in f1:
            s1=line.split()
            l1.append(s1)
        l2=[]
        for line in f2:
            s2=line.split()
            l2.append(s2)
        for i in range(0,20):
            l1[i].append(l2[i][1])
        sum=0
        for k in range(0,20):
            if l1[k][1]==l1[k][2]:
                sum=sum+4
            elif l1[k][1]=="-":
                sum=sum+0
            else:
                sum=(sum-1)
        print(sum)
    with open("Admin\\FinalReport.txt","a") as f3:
        f3.write(y+" ")
        f3.write(str(sum))
        f3.write("\n")



        
        

