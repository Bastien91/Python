# Exercice 14: Calcul mental
"""
On veut réaliser un programme de calcul mental.
Écrire un algorithme qui :
    - tire aléatoirement deux entiers entre 1 et 10,
    - demande de saisir le produit de ces deux entiers,
    - affichage "Gagné !" si le produit saisi est correct
    ou affiche "Perdu !" ainsi que le vrai résultat si le produit saisi est incorrect.

"""
from random import *

def Calcul_Mental():
    entier1 = randint(1, 10)
    entier2 = randint(1, 10)
    resultat = entier1 * entier2
    reponse = int(input("Quel est le produit de : " +str(entier1) +" * "+str(entier2) +" = "))
    
    if(resultat != reponse):
        print("Perdu!")
    else:
        print("Gagné!")
    
Calcul_Mental()
