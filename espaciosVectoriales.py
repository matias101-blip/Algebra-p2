#!/usr/bin/env python3

import numpy as np
from sympy import *
# 1.- V = [x,y] x**2 + y**2 <= 0
# 2.-
# 3.-
# 4,-
# 5.-

lista_axioma = []
x,y = symbols('x y')
x1,x2,y1,y2 = symbols('x1 x2 y1 y2')
V = np.array([x, y])
u = np.array([x1, y1])
v = np.array([x2, y2])

def axioma_1 ():
    # u + v = V
    C_x = u[0] + v[0]
    C_y = u[1] + v[1]
    C_x_s = f'{C_x}'
    C_y_s = f'{C_y}'

    if 'y' in C_y_s and 'x' in C_x_s:
        lista_axioma.append(1)

def axioma_2():
    # u + v = v + u
    Cu_v = [u[0]+v[0], u[1]+v[1]]
    Cv_u = [v[0]+u[0], v[1]+u[1]]

    if Cu_v == Cv_u:
        lista_axioma.append(2)


axioma_1()
axioma_2()
print(f'Los axiomas que se cumplen son los siguientes: {lista_axioma}')
