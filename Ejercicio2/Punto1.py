# -*- coding: utf-8 -*-
"""
TRABAJO 1: CALCULO PROPOSICIONAL
Daniel Felipe Yépez Taimal
Javier Urrego Castilla
Juan Camilo Arteaga Ibarra
Nuthelk Molina Cardona

Ejercicio 2. Punto 1
[(P ⇒ Q) ∧ (Q ⇔ R)] ⇒ (P ⇒ R)

Enlace Wolfram: https://www.wolframalpha.com/input/?i=%5B%28P%3D>Q%29%26%28Q<%3D>R%29%5DImplies%5B%28P%3D>R%29%5D
"""
from sympy import *
from sympy.logic.boolalg import is_cnf # forma normal conjuntiva
from sympy.logic.boolalg import is_dnf # forma normal disyuntiva
from sympy.logic import simplify_logic
from sympy.logic.boolalg import Equivalent
from sympy.abc import P, Q, R


Proposition = ((P >> Q) & (Equivalent(Q,R))) >> (P >> R)
#Proposition = ((P >> Q) & (Equivalent(Q,R))) >> (P >> R)

print("Ejercicio 1:\n")

print("Forma Normal Conjuntiva")
print("¿Es FNC?: ", is_cnf(((P >> Q) & (Equivalent(Q,R))) >> (P >> R)))
print(simplify_logic(Proposition, form='cnf'))
print("Forma Normal Conjuntiva Principal: No hay, porque es tautología")

print('\n')

print("Forma Normal Disyuntiva")
print("¿Es FND?: ", is_dnf(((P >> Q) & (Equivalent(Q,R))) >> (P >> R)))
print(simplify_logic(Proposition, form='dnf'))
print("Forma Normal Disyuntiva Principal: (P & Q & R) | (P & Q & ~R) | (P & ~Q & R) | (P & ~Q & ~R) | (~P & Q & R) | (~P & Q & ~R) | (~P & ~Q & R) | (~P & ~Q & ~R)")