# Exercice 3 : Bob et ses billes
"""
Bob possède un certain nombre de billes. Il veut regrouper ses billes dans des sacs, en mettant 17 billes par sac.
Écrire un algorithme qui :
    - demande de saisir un nombre de billes,
    - affiche le nombre de sacs qui seront pleins,
    - affiche le nombre de billes restantes.
"""
nombre_de_billes = int(input("Saisir le nombre de billes de Bob : "))
capcitee_du_sac = 17

nombre_sac_plein = nombre_de_billes // capcitee_du_sac
nombre_de_billes_restantes = nombre_de_billes % capcitee_du_sac

print("Nombre de sac plein : "+ str(nombre_sac_plein))
print("il reste "+ str(nombre_de_billes_restantes) +" billes")
