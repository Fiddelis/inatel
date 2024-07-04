from sympy import Symbol, solve, tan, sqrt

C = 206 % 10

def resultado(x, i):
    try:
        print(f'x{i} = {round(float(x), 3)}')
    except:
        complexa = complex(x)
        print(f'x{i} = {round(complexa.real, 3)} + {round(complexa.imag, 3)}j')

def equacao1(x):
    return 2**x + 2**(4*x) - (C + 1)

def equacao2(x):
    return 5*sqrt(x) - 4*x**2 + x/2 - C

def equacao3(x):
    return (3*tan((C - 3)*x) + 2)**2

if __name__ == '__main__':
    x = Symbol('x')

    resultadoEquacao1 = solve(equacao1(x))
    resultadoEquacao2 = solve(equacao2(x))
    resultadoEquacao3 = solve(equacao3(x))

    print('\n2**x + 2**4x = C + 1')
    for i, x in enumerate(resultadoEquacao1):
        resultado(x, i)

    print('\n5*sqrt(x) - 4x**2 + x/2 = C')
    for i, x in enumerate(resultadoEquacao2):
        resultado(x, i)

    print('\n{3tan[(C - 3)x] + 2}**2 = 0')
    for i, x in enumerate(resultadoEquacao3):
        print(f'x{i} = {x}')
