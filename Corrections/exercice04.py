# Exercice 4 : Bob part en voyage aux États-Unis
"""
Écrire un algorithme qui :
    - Demande de saisir une somme en euros, qui convertit cette somme en dollars (1 euro vaut environ 1,17 dollars) et qui affiche le résultat.
    - Bob veut ramener des chapeaux de cowboy de son voyage. Il trouve des chapeaux à 3,99 dollars pièce. 
    Compléter l'algorithme précédent en affichant combien de chapeaux pourront être achetés au maximum avec la somme saisie à la question précédente
    et combien il restera alors de dollars.
"""
euros = int(input("Saisir une somme d'argent en euros : "))
dollars = euros * 1.17
print("Conversion euros en dollars : "+str(dollars))

chapeau_cowboy = 3.99
nombre_chapeau_acheter = dollars // chapeau_cowboy
dollars_restants = dollars % chapeau_cowboy

print("Bob pourra acheter " + str(nombre_chapeau_acheter) + " chapeau de cowboy")
print("dollars restants : " + str(round(dollars_restants, 2)))
