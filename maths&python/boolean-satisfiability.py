def func(b1,b2,b3):
    fn = (b1 or b2) and (b1 or not (b2 and not b3)) and (not b2 and b3)
    return fn
for i in range(1,3):
    if i == 1:
        b1 = True
    else:
        b1 = False
    for j in range(1,3):
        if j == 1:
            b2 = True
        else:
            b2 = False
        for k in range(1,3):
            if k == 1:
                b3 = True
            else:
                b3 = False
            x = func(b1,b2,b3)
            if x == True:
                print("satisfiable")
                print(b1,b2,b3)
            break
        break
    break
        
if x != True:
    print("Unsatisfiable")
            
                    