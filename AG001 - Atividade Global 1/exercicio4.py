from sympy import Symbol, solve

C = 206 % 10

V1 = (C+2)*4
V2 = (C+1)*5

R1 = 12000
R2 = 4000
R3 = 6000

# Método das malhas

def malha1(i1, i2):
    return V1 - (R1*i1) - R3*(i1 - i2)

def malha2(i1, i2):
    return V2 - R3 * (i2 - i1) - (R2*i2)

if __name__ == '__main__':
    x = Symbol('i1')
    y = Symbol('i2')

    i1, i2 = solve((malha1(x, y), malha2(x, y))).values()
    i3 = i2 - i1

    print(f'i1 = {i1}')
    print(f'i2 = {i2}')
    print(f'i3 = {i3}')