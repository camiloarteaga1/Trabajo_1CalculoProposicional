# -*- coding: utf-8 -*-
"""
TRABAJO 1: CALCULO PROPOSICIONAL
Daniel Felipe Yépez Taimal
Javier Urrego Castilla
Juan Camilo Arteaga Ibarra
Nuthelk Molina Cardona

Ejercicio 2. Punto 3
[(P ⊻ Q) ⇔ (Q ⊻ P)] V (P ↓ Q)

Enlace Wolfram: https://www.wolframalpha.com/input/?i=%28%28%5BP%5DXor%5B+Q%5D%29<%3D>%28%5BQ%5DXor%5BP%5D%29%29%7C%7C%28%5BP%5DNor%5BQ%5D%29
"""
from sympy import *
from sympy.logic.boolalg import is_cnf # forma normal conjuntiva
from sympy.logic.boolalg import is_dnf # forma normal disyuntiva
from sympy.logic import simplify_logic
from sympy.logic.boolalg import Equivalent
from sympy.abc import P, Q, R


Proposition = (Equivalent((P ^ Q),(Q ^ P))) | (~P & ~Q)

print("Ejercicio 3:\n")

print("Forma Normal Conjuntiva")
print("¿Es FNC?: ", is_cnf((Equivalent((P ^ Q),(Q ^ P))) | (~P & ~Q)))
print(simplify_logic(Proposition, form='cnf'))
print("Forma Normal Conjuntiva Principal: No hay, porque es tautología")

print('\n')

print("Forma Normal Disyuntiva")
print("¿Es FND?: ", is_dnf((Equivalent((P ^ Q),(Q ^ P))) | (~P & ~Q)))
print(simplify_logic(Proposition, form='dnf'))
print("Forma Normal Disyuntiva Principal: (P & Q) | (~P & Q) | (P & ~Q) | (~P & ~Q)")
