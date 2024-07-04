from sympy import Symbol, Integral, Derivative, pi, cos

C = 206 % 10

A = 0.15  # m - Amplitude
F = 20  # Hz - Frequencia
W = 2 * pi * F  # Frequência angular

def minhaFuncao(t):
    return A * W * cos(W * t - C)

if __name__ == '__main__':
    t = Symbol('t')

    x = Integral(minhaFuncao(t), t).doit()
    v = minhaFuncao(t)
    a = Derivative(minhaFuncao(t), t).doit()

    a10 = a.subs({t: 10})

    print('\nDeslocamento: ')
    print(f'x(t) = {x}')

    print('\nVelocidade: ')
    print(f'v(t) = {v}')

    print('\nAceleracao: ')
    print(f'a(t) = {a}')

    print('\nAceleracao em t = 10: ')
    print(f'a(10) = {round(float(a10), 2)} m/s**2')
