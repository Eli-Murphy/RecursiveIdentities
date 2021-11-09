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

def power(base, exp):
    if exp != 1:
        return base * power(base,exp-1)
    if exp == 1:
        return base
    if exp == 0:
        return 1
    if exp < 0:
        return "Sorry, no negative exponents"

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

def main():
    base=2
    exp=-2
    print(power(base,exp))

if __name__ == '__main__':
    main()