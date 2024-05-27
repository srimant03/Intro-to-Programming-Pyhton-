#right angled triangle

print("Pattern Printing")
print("1. Right Angled Triangle")
print("2. Isosceles Triangle")
print("3. Kite")
print("4. Half Kite")
print("5. X")
pattern = int(input("Enter Type of Pattern: "))
n = int(input("Enter Size: "))

if pattern == 1:
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()

elif pattern == 2:
    for i in range(n):
        x = 2*n - 1
        y = x - 2*i + 1
        for j in range(y//2):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        for j in range(y//2):
            print(" ", end="")
        print()

elif pattern == 3:
    for i in range(n):
        x = 2*n - 1
        y = x - 2*i + 1
        for j in range(y//2):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        for j in range(y//2):
            print(" ", end="")
        print()
    for i in range(2*n - 3, 0, -2):
        x = 2*n - 1
        y = x - i + 1
        for j in range((y//2)+1):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        for j in range((y//2)+1):
            print(" ", end="")
        print()
    
elif pattern == 4:
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()
    for i in range(n-1):
        for j in range(n-1-i):
            print("*", end="")
        print()

elif pattern == 5:
    for i in range(2*n-1, 0, -2):
        x = 2*n - 1
        y = x - i + 1
        for j in range((y//2)+1):
            print(" ", end="")
        for j in range(i):
            if j == 0 or j == i-1:
                print("*", end="")
            else:
                print(" ", end="")
        for j in range((y//2)+1):
            print(" ", end="")
        print()
    for i in range(3, 2*n, 2):
        x = 2*n - 1
        y = x - i + 1
        for j in range((y//2)+1):
            print(" ", end="")
        for j in range(i):
            if j == 0 or j == i-1:
                print("*", end="")
            else:
                print(" ", end="")
        for j in range((y//2)+1):
            print(" ", end="")
        print()




        

