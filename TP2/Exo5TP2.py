#Exo 5 TP2

def deriver(f,a,h):
    return (f(a+h)-f(a))/h

def resoudre(f,a,h):
    while abs(f(a)) >= h:
        b = a - f(a) / deriver(f,a,h)
    return b

def f(x):
    return x*x - 2

print('sqrt(2) = ',resoudre(f,1,0.000001),sep='')