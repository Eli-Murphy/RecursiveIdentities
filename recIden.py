def factorial(n):
    if n == 0:
        return 1
    if n > 0:
        return n * factorial(n-1)

def summaration(n):
    if n == 1:
       return 1
    if n > 0:
       return n + summaration(n-1)

def power(base, exp):
    if exp > 1:
        return base * power(base,exp-1)
    if exp == 1:
        return base
    if exp == 0:
        return 1
    if exp < 0:
        #return "Sorry, no negative exponents"
        return (base * power(base,exp+1))

#def fibonacci(n): #Eli

#def sond(n): #Eli

#def pond(n): #Yash

#def potwn(a,b): #Eli

#def sonir("?"): #Yash UNKNOWN

#def revdig(n):#Eli

#def euclidGCD(x,y): #Yash

#def cib(p,r,t): #Eli

def sqrtbi(f,N,a,b):
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n)/2

def sqrtneuton(n,p,e):
    if abs(2*e - n) < p:    
        return e
    if e == n:
        return sqrtneuton((n,p,(e+n)/e)/2)
        

#def comboitem(n): #Yash

def main():
    base=2
    exp=-2
    if exp >= 0:
        print(power(base,exp))
    if exp < 0:
        print(1/power(base,exp))

if __name__ == '__main__':
    main()