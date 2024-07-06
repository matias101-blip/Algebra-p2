#!/usr/bin/env python3
#Espacios vectoriales ejercicio 1
import numpy as np
import sympy as sp
# 1.- V = [x,y]
lista_axioma = []
x,y = sp.symbols('x y')
x1,x2,y1,y2 = sp.symbols('x1 x2 y1 y2')
V = sp.simplify(np.array([x, y]))
u = np.array([x1, y1])
v = np.array([x2, y2])
v0 = np.array([0, 0])
c, d = sp.symbols('c d')

    # u + v = V
C_x = u[0] + v[0]
C_y = u[1] + v[1]
C_x_s = f'{C_x}'
C_y_s = f'{C_y}'

if 'y' in C_y_s and 'x' in C_x_s:
    lista_axioma.append(1)

    # u + v = v + u
Cu_v = [u[0]+v[0], u[1]+v[1]]
Cv_u = [v[0]+u[0], v[1]+u[1]]

if Cu_v == Cv_u:
    lista_axioma.append(2)

x3,y3 = sp.symbols('x3 y3')
w = np.array([x3, y3])
C_u_v_w = (u + v) + w
C_w_u_v = u + (v + w)
resultado = sp.simplify(C_u_v_w) == sp.simplify(C_w_u_v)
if resultado:
    lista_axioma.append(3)


#u + 0 = u
sum_0 = sp.simplify(u + 0)
resultado = sum_0 == sp.simplify(u)
if resultado:
    lista_axioma.append(4)

#u (-u) = 0
sum_U = sp.simplify(u + (-u))
v_0 = sp.simplify(v0)
if sum_U == v_0:
    lista_axioma.append(5)

#c * u = V
c = sp.simplify('c')
cu = sp.simplify(c * u)
cu_s = f'{cu}'
if 'x' in cu_s and 'y' in cu_s:
    lista_axioma.append(6)

#c(u+v) = cu + cv
c = sp.symbols('c')
resultado = sp.simplify(c*(u + v)) == sp.simplify(c*u + c*v)
if resultado:
    lista_axioma.append(7)

#(c+d)u = cu + du
resultado = sp.simplify((c+d)*u) == sp.simplify(c*u + d*u)
if resultado:
    lista_axioma.append(8)

#c(du) = (cd)u
resultado = sp.simplify(c*(d*u)) == sp.simplify((c*d)*u)
if resultado:
    lista_axioma.append(9)

#1u = u
resultado = sp.simplify(1 * u) == sp.simplify(u)
if resultado:
    lista_axioma.append(10)


print(f'Los axiomas que se cumplen son los siguientes: {lista_axioma}')
