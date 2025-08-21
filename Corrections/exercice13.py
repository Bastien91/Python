# Exercice 13 : Plus grand
"""
Écrire une fonction maximum prenant en paramètres 2 nombres entiers et retournant le plus grand des deux.
"""
def maximum(entier1, entier2):
    if(entier1 > entier2):
        return entier1
    else:
        return entier2

print(maximum(90,4))
