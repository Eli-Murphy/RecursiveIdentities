def factorial(n):
    if n == 1:
        return 1
    if n > 0:
        return n * f(n-1)

def summaration(n):
    if n == 1:
       return 1
    if n > 0:
       return n + summaration(n-1)

def power(n, p):
    if n > 0:
        return p * power(p,n-1)
    if n == 1:
        return 1

#def fibonacci(n): #Eli

#def sond(n): #Eli

#def pond(n): #Yash

#def potwn(a,b): #Eli

#def sonir("?"): #Yash UNKNOWN

#def revdig(n):#Eli

#def euclidGCD(x,y): #Yash

#def cib(p,r,t): #Eli

#def sqrtbi(n): #Yash

#def sqrtneuton(n,p,e)

#def comboitem(n): #Yash




# def what(a,b)
n = 10
p = 2
print(power(p, n))