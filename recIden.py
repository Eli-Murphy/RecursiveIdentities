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


# def fibonacci(n):

# def sond(n):

# def pond(n):

# def potwn(n):

# def sonir(n):

# def revdig(n):

# def euclid(n):

# def cib(n):

# def sqrtbi(n):

# def comboitem(n):




# def what(a,b)
n = 10
p = 2
print(power(p, n))