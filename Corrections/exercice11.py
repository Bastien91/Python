# Exercice 11 : Mot de passe
"""
Le mot de passe d'un ordinateur est "James-Bob".
Écrire un algorithme qui demande à l'utilisateur de saisir un mot de passe, et qui affiche un bip d'alarme si le mot de passe saisi est incorrect.
"""
mot_de_passe = input("Saisir un mot de passe")
if(mot_de_passe != "James-Bob"):
    print("Bip Bip! Mauvais mot de passe")
else:
    print("Mot de passe correct. Bienvenue!")
