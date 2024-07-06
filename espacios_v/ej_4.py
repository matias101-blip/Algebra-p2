#!/usr/bin/env python3
import sympy as sp

# 12 El conjunto de todas las ternas ordenadas de numeros reales (x,y,z)
x, x1, x2, x3, y, y1, y2, y3, z, z1, z2, z3, c, d = sp.symbols(
    "x x1 x2 x3 y y1 y2 y3 z z1 z2 z3 c d"
)
V = sp.Matrix([x, y, z])
u = sp.Matrix([x1, y1, z1])
v = sp.Matrix([x2, y2, z2])
w = sp.Matrix([x3, y3, z3])
lista_axiomas = []
sustituciones = {
    x1: x,
    x2: x,
    x1 + x2: x,
    y1: y,
    y2: y,
    y1 + y2: y,
    z1: z,
    z2: z,
    z1 + z2: z,
}

sustituciones_m = {c * x1: x, c * y1: y, c * z1: z}


def Suma(v_1, v_2):
    return sp.simplify(sp.Matrix([v_2[0], v_1[1] + v_2[1], v_2[2]]))


# 1⃣ Primer axioma: u + v = V
lista_axiomas.append(1) if Suma(u, v).subs(sustituciones) == V else None

# 2⃣ Segundo axioma: u + v = v + u
lista_axiomas.append(2) if Suma(u, v) == Suma(v, u) else None

# 3⃣ Tercer axioma: (u + v) + w = u + (v + w)
lista_axiomas.append(3) if Suma(Suma(u, v), w) == Suma(u, Suma(v, w)) else None

# 4⃣ Cuarto axioma: u + 0 = u
lista_axiomas.append(4) if Suma(u, [0, 0, 0]) == u else None

# 5⃣ Quinto axioma: u + (-u) = 0
lista_axiomas.append(5) if Suma(u, (-u)) == [0, 0, 0] else None

# 6⃣ Sexto axioma: c(u) = V
lista_axiomas.append(6) if (c * u).subs(sustituciones_m) == V else None

# 7⃣ Séptimo axioma: c(u + v) = cu + cv
(
    lista_axiomas.append(7)
    if sp.simplify(c * Suma(u, v)) == Suma((c * u), (c * v))
    else None
)

# 8⃣ Octavo axioma: (c + d)u = cu + du
(
    lista_axiomas.append(8)
    if ((c + d) * u) == sp.simplify(Suma((c * u), (d * u)))
    else None
)


# 9⃣ Noveno axioma: c(du) = (cd)u
lista_axiomas.append(9) if (c * (d * u)) == ((c * d) * u) else None

# 🔟 Décimo axioma: 1 * u = u
lista_axiomas.append(10) if (1 * u) == u else None

print(f"Los axiomas que se cumplen son: {lista_axiomas}")
