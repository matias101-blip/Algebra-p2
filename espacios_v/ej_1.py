#!/usr/bin/env python3
import sympy as sp

# 1 V es el conjunto de todos los pares ordenados de numeroa reales (x,y)
d, c, x1, x2, x3, y1, y2, y3, x, y = sp.symbols("d c x1 x2 x3 y1 y2 y3 x y")
V = sp.Matrix([x, y])
u = sp.Matrix([x1, y1])
v = sp.Matrix([x2, y2])
w = sp.Matrix([x3, y3])

lista_axiomas = []

# Primer axioma u + v = V
u_v = u + v
if u_v[0] == x1 + x2:
    u_v[0] = x
    if u_v[1] == y1 + y2:
        u_v[1] = y
if u_v == V:
    lista_axiomas.append(1)

# Segundo axioma u + v = v + u
u_v = sp.simplify(u + v)
v_u = sp.simplify(v + u)
if u_v == v_u:
    lista_axiomas.append(2)

# 3rd axioma (u+v) + w = u + (v+w)
u_v_w = sp.simplify((u + v) + w)
if u_v_w == sp.simplify(u + (v + w)):
    lista_axiomas.append(3)

# 4to axioma u + 0 = u
u_0 = sp.Matrix([sp.simplify(u[0] + 0), sp.simplify(u[1] + 0)])
if u_0 == u:
    lista_axiomas.append(4)

# 5to axioma u+(-u)=0
u_u = sp.simplify(u + (-u))
if u_u == sp.Matrix([0, 0]):
    lista_axiomas.append(5)

# 6to axioma c(u) = V
c_u = sp.simplify(c * (u))
if c_u[0] == c * x1 and c_u[1] == c * y1:
    lista_axiomas.append(6)

# 7mo axioma c(u + v) = cu + cv
c_u_v = sp.simplify(c * (u + v))
if c_u_v == sp.simplify(c * u + c * v):
    lista_axiomas.append(7)

# 8vo axioma (c + d)*u = c*u + d*u
c_d_u = sp.simplify((c + d) * u)
if c_d_u == sp.simplify(c * u + d * u):
    lista_axiomas.append(8)

# 9no axioma c(du) = (cd)u
c_d_u = sp.simplify(c * (d * u))
if c_d_u == sp.simplify((c * d) * u):
    lista_axiomas.append(9)

# 10mo axioma 1 * u = u
u_1 = sp.Matrix([1 * u[0], 1 * u[1]])
if u_1 == u:
    lista_axiomas.append(10)

print(f"Los axiomas que se cumplen son: {lista_axiomas}")
