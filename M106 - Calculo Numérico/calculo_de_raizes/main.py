def func(x):
    return -x**2 + 2*x + 1
def dfunc(x):
    return -2*x + 2

intervalo_esquerda = -3
intervalo_direita = 3
intervalo = []
raizes = []

for i in range(intervalo_esquerda, intervalo_direita + 1):
    intervalo.append(i)


# 1
for x in intervalo:
    if (func(x) * func(x + 1) < 0) and (dfunc(x) * dfunc(x + 1) > 0):
        raizes.append([x, x+1])

print(f'Raizes = {raizes}')

# 2 [-1, 0]
a, b = raizes[0]
parada = 0.05

fa_negativo = func(a) < 0
n = 0
while True:
    xn = (a + b) / 2
    fx = func(xn)
    e = abs(fx)

    fx_negativo = fx < 0

    if fa_negativo == fx_negativo:
        a = xn
    else:
        b = xn
    
    if e < parada: break

    n += 1
print("---------------")
print("Bissecção")
print(f'n = {n}, Xn = {xn}\nCritério de parada = {parada}')

# 3 [2, 3]
a, b = raizes[1]
n = 0
xn = (a + b) / 2
parada = 0.05
while True:
    fx = func(xn)
    dfx = dfunc(xn)
    xn -= (fx / dfx)
    e = abs(fx)

    if e < parada: break
    n += 1

print("---------------")
print("Newtown-Raphson")
print(f'n = {n}, Xn = {xn}\nCritério de parada = {parada}')