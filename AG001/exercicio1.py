from sympy import Symbol, Limit, S

C = 206 % 10

def minhaFuncao(x):
    return (1 + (C + 4) / (x**3)) ** (x**3)


if __name__ == '__main__':
    x = Symbol('x')

    result = Limit(minhaFuncao(x), x, 0).doit()
    print(f'\nX -> 0: {result}')

    result = Limit(minhaFuncao(x), x, S.Infinity).doit()
    print(f'\nX -> oo: {result}')

    result = Limit(minhaFuncao(x), x, -S.Infinity).doit()
    print(f'\nX -> -oo: {result}')
