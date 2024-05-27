#coefficients of the polynomial are always 1
#power of x is stored in the list exp
#x is the initial guesss
#threshold is 0.0001

def fun(x, exp):
    fun = 0
    for i in range(len(exp)):
        fun += x**exp[i]
    return fun

def derivative(x, exp):
    derivative = 0
    for i in range(len(exp)):
        derivative += exp[i]*x**(exp[i]-1)
    return derivative

def newton_raphson(x, exp):
    h = fun(x, exp)/derivative(x, exp)
    while abs(h) >= 0.0001:
        h = fun(x, exp)/derivative(x, exp)
        x = x - h
    return x

exp = [2, 1]
x = 1

print(newton_raphson(x, exp))

