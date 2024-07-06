#!/usr/bin/env python3

# Ejercico 2
import sympy as sp

d, c, y1, y2, z1, z2, y3, z3, y, z = sp.symbols("d c y1 y2 z1 z2 y3 z3 y z")
V = sp.Matrix([0, y, z])
u = sp.Matrix([0, y1, z1])
v = sp.Matrix([0, y2, z2])
w = sp.Matrix([0, y3, z3])
v0 = sp.Matrix([0, 0, 0])

lista_axiomas = []


def regla_m(vector, constante):
    resultado = []
    for item in vector:
        if item == y1 or item == y2:
            resultado.append(0)
        else:
            resultado.append(sp.simplify(constante * item))
    return sp.Matrix(resultado)


# Primer axioma u + v = V
u_v = u + v
if u_v[1] == y1 + y2 and isinstance(u_v[0], (int, float, complex)):
    u_v[1] = y
    if u_v[2] == z1 + z2:
        u_v[2] = z
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
u_0 = sp.simplify(u + v0)
if u_0 == u:
    lista_axiomas.append(4)

# 5to axioma u+(-u)=0
u_u = sp.simplify(u + (-u))
if u_u == v0:
    lista_axiomas.append(5)

# 6to axioma c(u) = V
c_u = []
for item in u:
    if item == y1:
        c_u.append(0)
    else:
        c_u.append(sp.simplify(c * item))

if isinstance(c_u[0], (int, float, complex)) and c_u[1] == c * y1 and c_u[2] == c * z1:
    lista_axiomas.append(6)

# 7mo axioma c(u + v) = cu + cv
c_u_v = regla_m(sp.simplify(u + v), c)
if c_u_v == sp.simplify(regla_m(u, c) + regla_m(u, c)):
    lista_axiomas.append(7)

# 8vo axioma (c + d)*u = c*u + d*u
c_d_u = regla_m(u, sp.simplify(c + d))
if c_d_u == sp.simplify(regla_m(u, c) + regla_m(u, d)):
    lista_axiomas.append(8)

# 9no axioma c(du) = (cd)u
c_d_u = sp.simplify(c * (regla_m(u, d)))
if c_d_u == regla_m(u, sp.simplify(c * d)):
    lista_axiomas.append(9)

# 10mo axioma 1 * u = u
u_1 = regla_m(u, 1)
if u_1 == u:
    lista_axiomas.append(10)

print(f"Los axiomas que se cumplen son: {lista_axiomas}")
