#!/usr/bin/env python3
#!/usr/bin/env python3
import sympy as sp

# 13 El conjunto de todas las ternas ordenadas de numeros reales (x,y,z)
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


def Multi(v_1, c):
    return sp.simplify(sp.Matrix([v_1[0], 1, v_1[2]]))


# 1⃣ Primer axioma: u + v = V
lista_axiomas.append(1) if (u + v).subs(sustituciones) == V else None

# 2⃣ Segundo axioma: u + v = v + u
lista_axiomas.append(2) if (u + v) == (v + u) else None

# 3⃣ Tercer axioma: (u + v) + w = u + (v + w)
lista_axiomas.append(3) if ((u + v) + w) == (u + (v + w)) else None

# 4⃣ Cuarto axioma: u + 0 = u
lista_axiomas.append(4) if (u + sp.Matrix([0, 0, 0])) == u else None

# 5⃣ Quinto axioma: u + (-u) = 0
lista_axiomas.append(5) if (u + (-u)) == sp.Matrix([0, 0, 0]) else None

# 6⃣ Sexto axioma: c(u) = V
lista_axiomas.append(6) if (Multi(u, c)).subs(sustituciones_m) == V else None

# 7⃣ Séptimo axioma: c(u + v) = cu + cv
(
    lista_axiomas.append(7)
    if sp.simplify(Multi((u + v), c)) == ((Multi(u, c)) + (Multi(v, c)))
    else None
)
# 8⃣ Octavo axioma: (c + d)u = cu + du
(
    lista_axiomas.append(8)
    if (Multi(u, (c + d))) == sp.simplify((Multi(u, c)) + (Multi(u, d)))
    else None
)

# 9⃣ Noveno axioma: c(du) = (cd)u
lista_axiomas.append(9) if (Multi((Multi(u, d)), c)) == (Multi(u, (c * d))) else None

# 🔟 Décimo axioma: 1 * u = u
lista_axiomas.append(10) if (Multi(u, 1)) == u else None

print(f"Los axiomas que se cumplen son: {lista_axiomas}")
