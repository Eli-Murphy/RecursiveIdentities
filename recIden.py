
rev = 0

def factorial(n):
    if n == 0:
        return 1
    if n > 0:
        return n * factorial(n-1)

def summation(n):
    if n == 1:
       return 1
    if n > 0:
       return n + summation(n-1)

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

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return(fibonacci(n-1) + fibonacci(n-2))

def sond(n):
    if n == 0:
        return 0
    if n != 0:
        return((n % 10) + (n//10))

#def pond(n): #Yash

def potwn(a,b):
    if a < b:
        return potwn(b,a)
    elif b != 0:
        return (a + potwn(a,b-1))
    else:
        return 0


#def sonir("?"): #Yash UNKNOWN

def revdig(n):
    if n > 0:
        global rev
        ones = n % 10
        rev = rev * 10 + ones
        revdig(int(n/10))
        return rev

#def euclidGCD(x,y): #Yash

def cib(p,r,t):
    if t == 0:
        return p
    if t > 0:
        return ((1+r) * cib(p,r,t-1))

def sqrtbi(n):
    '''Approximate solution of f(x)=0 on interval [a,b] by bisection method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    x_N : number
        The midpoint of the Nth interval computed by the bisection method. The
        initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
        midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iteration, the bisection method fails and return None.
    '''

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
    choice = input("Function: ")
    if choice == "exponent":
        base=2
        exp=-2
        if exp >= 0:
            print(power(base,exp))
        if exp < 0:
            print(1/power(base,exp))
    if choice == "factorial":
        n=5
        print(factorial(n))
    if choice == "summation":
        n=5
        print(summation(n))
    if choice == "fibonacci":
        n=10
        print(fibonacci(n))
    if choice == "sond":
        n=12
        print(sond(n))
    if choice == "potwn":
        a=11
        b=22
        print(potwn(a,b))
    if choice == "revdig":
        n = -11263
        print(revdig(n))
    if choice == "cib":
        p = 1200
        r = 5.4
        t = 2
        print(cib(p,r,t))

if __name__ == '__main__':
    main()