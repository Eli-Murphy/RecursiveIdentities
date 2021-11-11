
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
    return (n % 10 + sond(int(n / 10)))

def pond(n):
    if n == 0:
        return 0
    return (n % 10 * sond(int(n / 10)))

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
    if choice == "pond":
        n=20
        print(pond(n))

def upgradedMain():
    print("Welcome to the recursive function's calculator!\n")
    while True:
        print(r"""
    Please enter a number 1-13

    1. Factorial of a number
    2. Summation of a number
    3. Power/exponential function
    4. Fibonacci’s numbers
    5. Sum of a number’s digits
    6. Product of number’s digits
    7. Product of two whole numbers
    8. Sum of numbers in a range
    9. Reverse the digits in a number
    10. Euclid’s GCD algorithm
    11. Find a compound interest balance
    12. Find a square root using the bisection method
    13. Find combinations of item 
    14. Find a square root using Newton's method
        """)
        choice = input("Enter Here: ")
        try:
            choice = str(choice)
            if choice == "1":
                n = input("What number would you like to be factorialed?: ")
                print("The factorial of ", n, " is ", factorial(n))
            elif choice == "2":
                n = input("What number are you tooking to find the summation of?: ")
                print("The summation of ", n, " is ", summation(n))
            elif choice == "3":
                base = input("What is the base of the equation?: ")
                exp = input("What is the exponent of the equation?: ")
                print(base, " to the power of ", exp, " is ", power(base,exp))
            elif choice == "4":
                n = input("What is the number you would like to put into the Fibonacci equation?: ")
                print(n, " put into the Fibonacci equation returns ", fibonacci(n))
            elif choice == "5":
                n = input("What number would you like to find the sum of its digits?: ")
                print("The sum of the digits of ", n, " is ", sond(n))
            elif choice == "6":
                n = input("What number would you like to find the product of its digits?: ")
                print("The product of the digits of ", n, " is ", pond(n))
            elif choice == "7":
                print("What two digits would you like to multiply?")
                a = input("Number 1: ")
                b = input("Number 2: ")
                print(a, " times ", b, " is ", potwn(a,b), ".")
            elif choice == "8":
                n = ("What number would you like to find the sum of the digits in it's range?: ")
                print("The sum of the digits in ", n, " in a range equals ", sonir(n), ".")
            elif choice == "9":
                n = ("What is the number that you would like to reverse the digits of?: ")
                print(n, " reversed is ", revdig(n), ".")
            elif choice == "10":
                print("Please input the two numbers you would like to find the GCD of using Euclid's Algorithm. ")
                a = input("Number 1: ")
                b = input("Number 2: ")
                print("The GCD of ", a, " and ", b, " is ", euclidGCD(a,b))
            elif choice == "11":
                print("Please input the required data to calculate the compund interest balance.")
                p = input("Principle: ")
                r = input("Rate: ")
                t = input("Time (years): ")
                print("The compound interest balance of the data inputted is ", cib(p,r,t))
            elif choice == "12":
                n = input("Please input the number you would like to find the square root of using the bisection method:")
                print("The square root of ", n, " is ", sqrtbi(n))
            elif choice == "13":
                #WHAT DOES THIS MEAN
                print("Sorry, this is currently work in progress.")
            elif choice == "14":
                print("Sorry, this is currently work in progress.")
        except:
            print("Please input a number 1-14")
if __name__ == '__main__':
    upgradedMain()