def word_count():
    s=str(input("Enter word:"))
    fname="question1_input.txt"
    f = open(fname,"r")
    count=0
    for line in f:
        s1=line.split()
        for i in s1:
            if i==s:
                count=count+1
    f.close()
    return count
def unique_words():
    fname="question1_input.txt"
    f=open(fname,"r")
    l=[]
    for line in f:
        s=line.split()
        for i in s:
            if i not in l:
                l.append(i)
                print(";",i, end=" ")
    f.close()
    print("\n")
def all_count():
    fname="question1_input.txt"
    f=open(fname,"r")
    d={}
    for line in f:
        s=line.split()
        for i in s:
            if i not in d:
                d[i]= 1
            else:
                d[i] += 1
    for x,y in d.items():
        print(x," : ",y)
    f.close()

def replace_words():
    x=str(input("Enter word to be replaced:"))
    y=str(input("Enter word that will replace:"))
    fname="question1_input.txt"
    f=open(fname,"r")
    l=(f.readlines())
    l1=[]
    for i in l:
        l1.append(i.split())
    n=len(l1)
    for i in range(0,n):
        for j in l1[i]:
            k = l1[i].index(j)
            if j==x:
                l1[i][k]=y
    f.close()
    f=open(fname,"w")
    for i in range(0,n):
        n1=len(l1[i])
        for j in range(0,n1):
            f.writelines(l1[i][j]+" ")
        f.writelines("\n")
    f.close()
    print("Replaced successfully")

while 1>0:
    print("-"*50)
    print("Enter your choice:")
    print("1. Display specific Word Count")
    print("2. Display Unique Words")
    print("3. Display all Word Counts")
    print("4. Replace Words")
    print("5. Quit")
    n=int(input("Enter your choice of operation:"))
    if n==1:
        y=word_count()
        if y==0:
            print("Word does not exist")
        else:
            print("Word Count:", y)
    if n==2:
        print("Unique Words:")
        unique_words()
    if n==3:
        print("Word Counts:")
        all_count()
    if n==4:
        replace_words()
    if n==5:
        quit()

