# Exercice 15: Vacances
"""
Bob ne va pas à la plage que si l'une des deux conditions suivantes au moins est satisfaite :
    - la température de l'air est supérieure à 25 degrés,
    - La température de l'eau est supérieure à 20 degrés.
Écrire un algorithme demandant la température de l'eau et de l'air,
et affichant un message si Bob peut aller à la plage.
"""

def Vacances():
    temperature_air = int(input("Saisir la température de l'air : "))
    temperature_eau = int(input("Saisir la température de l'eau : "))
    
    if(temperature_air > 25 or temperature_eau > 20):
        print("Bob peut aller à la plage.")
    else:
        print("Bob ne peut pas aller à la plage")

Vacances()
