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

#def sqrtneuton(n,p,e)

#def comboitem(n): #Yash




# def what(a,b)
n = 10
p = 2
print(power(p, n))