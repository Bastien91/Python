from random import *

# Exercice 9 : 
"""
Écrire une fonction deux_des qui ne prend pas de paramètre et retourne deux entiers aléatoires entre 1 et 6.
"""

def Deux_Des():
    premier_entier_aleatoire = randint(1, 6)
    deuxieme_entier_aleatoire = randint(1, 6)
    return premier_entier_aleatoire, deuxieme_entier_aleatoire

entier_aleatoire1, entier_aleatoire2 = Deux_Des()

print("Valeur Dè 1 : " +str(entier_aleatoire1))
print("Valeur Dè 2 : " +str(entier_aleatoire2))
