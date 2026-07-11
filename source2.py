import numpy as np
import matplotlib.pyplot as plt
import pygame

#dans ce cequi suit je tenterai de reoudre l'equation de diffusion de la chaleur en 1D avec la methode des differences finies explicites.
"""Après discrétisation de l'espace et du temps, on obtient une équation de la forme : T[i, j+1] = T[i, j]*A(K), où A(k) est une matrice de coefficients dépendant de la 
"conductivité thermique K et des pas de temps et d'espace. A(k)=coskdelta_x-i(V*delta_t/delta_x)*sin(k*delta_x). """
