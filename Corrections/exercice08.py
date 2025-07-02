
# Exercice 8 : 
"""
Écrire une fonction echange prenant en paramètres d'entrée deux nombres entiers et retournant ces entiers dans l'ordre inverse.
"""
def Echange(pEntier1, pEntier2):
    return pEntier2, pEntier1

# Appel de la Fonction

entier1 = 2
entier2 = 5

entier1_echange, entier2_echange = Echange(entier1, entier2)

print("entier 1 = "+str(entier1) + " et l'entier1 échangé = "+str(entier1_echange))
print("entier 2 = "+str(entier2) + " et l'entier2 échangé = "+str(entier2_echange))

