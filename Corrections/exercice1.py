
# Exercice 1 : Affichage age
"""
Faire un programme qui affiche ton âge : 
  - tu rentre ta date de naissance et le programme doit afficher ton âge
"""
annee_actuelle = 2025
annee_naissance = int(input("Saisir ton année de naissance : "))

age = annee_actuelle - annee_naissance

print("Tu as "+ str(age) +" ans")
