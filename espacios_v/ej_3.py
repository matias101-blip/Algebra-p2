#!/usr/bin/env python3
import sympy as sp

# 3 V es el conjunto de todos los polinomios de la forma
# at**2 + bt + c donde a,b y c son numeros reales, y b = a + 1

a, c, a1, b, c1, a2, c2, a3, c3, t, b1, b2, b3, d, e = sp.symbols(
    "a c a1 b c1 a2 c2 a3 c3 t b1 b2 b3 d e"
)
V = a * t**2 + b * t + c
u = a1 * t**2 + b1 * t + c1
v = a2 * t**2 + b2 * t + c2
w = a3 * t**2 + b3 * t + c3

lista_axiomas = []

# 1⃣ Primer axioma u + v = V
u_v = sp.collect(u + v, t)
u_v = u_v.subs({b1: a1 + 1, b2: a2 + 1})
u_v = u_v.as_ordered_terms()
regla = {b1: a1 + 1, b2: a2 + 1, b: a + 1}

(
    lista_axiomas.append(1)
    if c1 in u_v
    and c2 in u_v
    and sp.simplify(t**2 * (a1 + a2)) in u_v
    and sp.simplify(t * (b1 + b2)) in u_v
    else None
)

# 2⃣ Segundo axioma u + v = v + u
(
    lista_axiomas.append(2)
    if sp.collect(u + v, t).subs({b1: a1 + 1, b2: a2 + 1})
    == sp.collect(v + u, t).subs({b1: a1 + 1, b2: a2 + 1})
    else None
)

# 3⃣ axioma (u+v) + w = u + (v+w)
(
    lista_axiomas.append(3)
    if sp.collect((u + v) + w, t) == sp.collect(u + (v + w), t)
    else None
)

# 4⃣ axioma u + 0 = u
lista_axiomas.append(4) if sp.collect(u + 0, t) == sp.collect(u, t) else None

# 5⃣ axioma u+(-u)=0
lista_axiomas.append(5) if sp.collect(u + (-u), t) == 0 else None

# 6⃣ axioma c(u) = V
(
    lista_axiomas.append(6)
    if sp.expand(d * V)
    == sp.expand((d * a) * t**2 + (d * b) * t + d * c).subs({b: a + 1})
    else None
)

# 7⃣ c(u + v) = cu + cv
(
    lista_axiomas.append(7)
    if sp.expand(c * (u + v)).subs(regla)
    == (sp.expand(c * u) + sp.expand(c * v)).subs(regla)
    else None
)

# 8⃣ axioma (c + d)*u = c*u + d*u
(
    lista_axiomas.append(8)
    if sp.expand((d + e) * u).subs(regla)
    == (sp.expand(d * u) + sp.expand(e * u)).subs(regla)
    else None
)
# 9⃣ axioma c(du) = (cd)u
(
    lista_axiomas.append(9)
    if sp.expand(d * sp.expand(e * u)).subs(regla) == sp.expand((d * e) * u).subs(regla)
    else None
)
# 10mo axioma 1 * u = u
lista_axiomas.append(10) if sp.expand(1 * u) == u else None
print(f"Los axiomas que se cumplen son: {lista_axiomas}")
