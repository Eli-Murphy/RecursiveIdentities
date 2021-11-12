
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
        return 1/3(base * power(base,exp+1))

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

def pond(p,r,t): 
    if t == 0:
        return p
    if t > 0:
        return (1+r) * pond(p,r,t-1)

def pond(n):
    if n == 0:
        return 0
    return (n % 10 * pond(int(n / 10)))

def potwn(a,b):
    if a < b:
        return potwn(b,a)
    elif b != 0:
        return (a + potwn(a,b-1))
    else:
        return 0


def sonir(n): 
    if n < 10:
        return n
    if n > 10:
        return S(n+10) + (n % 10)

def revdig(n):
    if n > 0:
        global rev
        ones = n % 10
        rev = rev * 10 + ones
        revdig(int(n/10))
        return rev

def euclidGCD(x,y): 
    if y <= x and x % y == 0:
        return y
    if y >= x and x % y != 0:
        return euclidGCD(y, x % y)

def cib(p,r,t):
    if t == 0:
        return p
    if t > 0:
        return (1+r) * pond(p,r,t-1)

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

def sqrtneuton(x,e,a):
    if abs(a*a - x) < e:    
        return a
    else:
        a = (a * a + x) / (2 * a)
        return 1 * sqrtneuton(x,e,a)
        

#def comboitem(n): #Yash

def upgradedMain():
    print("Welcome to the recursive function's calculator!\n")
    while True:

        choice = input("Menu input here: ")

                    
        if choice == "1":
            n = input("What number would you like to be factorialed? (Positive): ")
            n = int(n)
            try:
                n = int(n)
                print("\nThe factorial of", n, "is", str(factorial(n)) + ".\n")
            except:
                print("\nPlease Input an integer number. \n")


        elif choice == "2":
            n = input("What number are you tooking to find the summation of? (Positive): ")
            try:
                n = int(n)
                print("\nThe summation of", n, "is", str(summation(n)) + ".\n")
            except:
                print("\nPlease Input an integer number. \n")


        elif choice == "3":
            base = input("What is the base of the equation?: ")
            exp = input("What is the exponent of the equation?: ")
            try:
                base = int(base)
                exp = int(exp)
                print(base, " to the power of", exp, "is", str(power(base,exp)) + ".\n")
            except:
                print("\nPlease verify your inputs are integers. \n")


        elif choice == "4":
            n = input("What is the number you would like to put into the Fibonacci equation?: ")
            try:
                n = int(n)
                print(n, "put into the Fibonacci equation returns", str(fibonacci(n))+ ".\n")
            except:
                print("\nPlease Input an integer number greater than zero. \n")


        elif choice == "5":
            n = input("What number would you like to find the sum of its digits?: ")
            try:
                n = int(n)
                print("The sum of the digits of ", n, " is ", sond(n), ".\n")
            except:
                print("\nPlease input an integer number. \n")


        elif choice == "6":
            
            n = input("What number would you like to find the product of its digits?: ")
            try:
                n = int(n)
                print("The product of the digits of", n, "is", pond(n) + ".\n")
            except:
                print("\nPlease input an integer number. \n")


        elif choice == "7":
            print("What two digits would you like to multiply?")
            a = input("Number 1: ")
            b = input("Number 2: ")
            try:
                a = int(a)
                b = int(b)
                print(a, " times", b, "is", potwn(a,b)+ ".\n")
            except:
                print("\nPlease verify your inputs are integers. \n")


        elif choice == "8":
            n = ("What number would you like to find the sum of the digits in it's range?: ")
            try:
                n = int(n)
                print("The sum of the digits in", n, "in a range equals", sonir(n)+ ".\n")
            except:
                print("\nPlease input an integer number. \n")



        elif choice == "9":
            n = ("What is the number that you would like to reverse the digits of?: ")
            try:
                n = int(n)
                print(n, " reversed is ", revdig(n), ".\n")
            except:
                print("\nPlease input an integer number. \n")



        elif choice == "10":
            print("Please input the two numbers you would like to find the GCD of using Euclid's Algorithm. ")
            a = input("Number 1: ")
            b = input("Number 2: ")
            try:
                a = int(a)
                b = int(b)
                print("The GCD of ", a, " and ", b, " is ", euclidGCD(a,b), ".\n")
            except:
                print("\nPlease verify your inputs are integers. \n")



        elif choice == "11":
            print("Please input the required data to calculate the compund interest balance.")
            p = input("Principle: ")
            r = input("Rate: ")
            t = input("Time (years): ")
            try:
                p = int(p)
                r = int(r)
                t = int(t)
                print("The compound interest balance of the data inputted is ", cib(p,r,t), ".\n")
            except:
                print("\nPlease verify your inputs are integers. \n")



        elif choice == "12":
            n = input("Please input the number you would like to find the square root of using the bisection method:")
            try:
                n = int(n)
                print("The square root of ", n, " is ", sqrtbi(n), ".\n")
            except:
                print("\nPlease input an integer number. \n")



        elif choice == "13":
            #WHAT DOES THIS MEAN
            print("Sorry, this is currently work in progress.")
            print("Please input the required data to calculate the compund interest balance.")
            x = input("Assumed Sqrt: ")
            e = input("epsilon: ")
            a = input("Correct root: ")
            try:
                x = float(x)
                e = float(e)
                a = float(a)
                print("The compound interest balance of the data inputted is ", sqrtneuton(x,e,a), ".\n")
            except:
                print("\nPlease verify your inputs are integers. \n")



        elif choice == "14":
            print("Sorry, this is currently work in progress.NEWTON")
 


        elif choice == "exit":
            break

        else:
            print("\nSorry, that is not a menu option. Please choose an option from the menu\n")

if __name__ == '__main__':

    from art import *
    tprint("     Welcome!\n\n")
    tprint("        MENU", font="cybermedium")
    print("""    ________________________________________________________
    |Please enter a number 1-13                            |
    |                                                      |
    |   1. Factorial of a number                           |
    |   2. Summation of a number                           |
    |   3. Power/exponential function                      |
    |   4. Fibonacci’s numbers                             |
    |   5. Sum of a number’s digits                        |
    |   6. Product of number’s digits                      |
    |   7. Product of two whole numbers                    |
    |   8. Sum of numbers in a range                       |
    |   9. Reverse the digits in a number                  |
    |   10. Euclid’s GCD algorithm                         |
    |   11. Find a compound interest balance               |
    |   12. Find a square root using the bisection method  |
    |   13. Find combinations of item                      |
    |   14. Find a square root using Newton's method       |
    |   Enter "exit" to close program                      |
    |______________________________________________________|
        """)
    upgradedMain()