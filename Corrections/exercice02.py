# Exercice 2 : Epicerie
"""
Une épicerie vend de la farine à 2 euros le kilo, et des tablettes de chocolat à 2,5 euros.
Écrire un algorithme qui :
    - demande de saisir un nombre de kilos de farine,
    - demande de saisir un nombre de tablettes de chocolat,
    - affiche le prix à payer au total pour la farine et le chocolat.
"""
nombre_kilos_farine = int(input("Saisir un nombre de kilos de farine : "))
nombre_tablettes_chocolat = int(input("Saisir un nombre de tablettes de chocolat : "))

prix_kilo_farine = 2
prix_tablette_chocolat = 2.5

prix_total = prix_kilo_farine * nombre_kilos_farine + prix_tablette_chocolat * nombre_tablettes_chocolat

print("Le prix total pour la farine et le chocolat est égal à "+ str(prix_total) +" euros")
