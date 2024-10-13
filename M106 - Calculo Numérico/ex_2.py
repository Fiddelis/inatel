def func_x(y, z):
    return (-2 + y - 2*z)/2
def func_y(x, z):
    return (-1 - x - z)/2
def func_z(x, y):
    return (1 + 2 * x + y)/(-3)
def e_x(x, k):
    return x[k] - x[k-1]

x = [0]
y = [0]
z = [0]
k = 1

x.insert(k, func_x(y[k-1],z[k-1]))
y.insert(k, func_y(x[k],z[k-1]))
z.insert(k, func_z(x[k],y[k]))

while abs(e_x(x, k)) >= 0.001 or abs(e_x(y, k)) >= 0.001 or abs(e_x(z, k)) >= 0.001:
    k = k + 1
    x.insert(k, func_x(y[k-1], z[k-1]))
    y.insert(k, func_y(x[k], z[k-1]))
    z.insert(k, func_z(x[k], y[k]))

print('x:',x[-1])
print('y:',y[-1])
print('z:',z[-1])
