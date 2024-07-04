from sympy import Symbol, Integral

C = 206 % 10

def minhaFuncao(x):
    return x**3 - 4*x**2 + 5*x - C

if __name__ == '__main__':
    x = Symbol('x')
    result = Integral(minhaFuncao(x), (x, 0, 5)).doit()
    print(result)
