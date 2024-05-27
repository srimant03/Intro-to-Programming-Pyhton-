def getReverse(n):
    while n != 0:
        i = n%10
        n = n//10
        print(i,end="")

def checkPalindrome(n):
    x = n
    rev=""
    while n!=0:
        i = n%10
        n = n//10
        i = str(i)
        rev = rev+i 
    rev = int(rev)
    if rev == x:
        print("True")
    else:
        print("False")

def checkNarcissistic(n):
    x = n
    sum = 0
    while n!=0:
        i = n%10
        n = n//10
        l = str(x)
        p = len(l)
        y = i**p
        sum = sum + y
    if sum == x:
        print("True") 
    else:
        print("False")

def findDigitSum(n):
    sum = 0
    while n!=0:
        i = n%10
        n = n//10
        sum = sum + i
    return sum


def findSquareDigitSum(n):
    sum = 0
    while n!= 0:
        i = n%10
        n = n//10
        sum = sum + i**2
    return sum

for i in range(1000):
    print("Hello User,Welcome to the application.Please select one of the following operations.")
    print("1.Find reverse of a number.")
    print("2.Check whether the number is a palindrome or not.")
    print("3.Check whether the number is a narcissistic number or not.")
    print("4.Find sum of digits of the number.")
    print("5.Find sum of squares of digits of the number.")
    print("6.Select 6 to exit the application.")

    a = int(input("Select the operation number you wish to perform:"))
    if a == 1:
        n = int(input("Enter number:"))
        if n>=0:
            getReverse(n)
        else:
            ("ERROR:Please enter non-negative input only")
    elif a == 2:
        n = int(input("Enter number:"))
        if n>=0:
            checkPalindrome(n)
        else:
            ("ERROR:Please enter non-negative input only")
    elif a == 3:
        n = int(input("Enter number:"))
        if n>=0:
            checkNarcissistic(n)
        else:
            ("ERROR:Please enter non-negative input only")
    elif a == 4:
        n = int(input("Enter number:"))
        if n>=0:
            y1 = 0
            y=findDigitSum(n)
            while y>= 10:
                y1 = y1 + y
                y = findDigitSum(y)
            print(y1 + y)
        else:
            ("ERROR:Please enter non-negative input only")
    elif a == 5:
        n = int(input("Enter number:"))
        if n>=0:
            y1 = 0
            y = findSquareDigitSum(n)
            while y>=10:
                y1 = y1 + y
                y = findSquareDigitSum(y)
            print(y1 + y)
        else:
            ("ERROR:Please enter non-negative input only")
    elif a == 6:
        break
    print("")


    


















    

        

