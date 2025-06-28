# Exercice 5 : Distributeur
"""
Écrire un programme qui demande de saisir une somme en centimes, puis
qui donne le nombre de pièces minimum de 2 centimes et 1 centime nécessaires pour payer cette somme.

Par exemple, si l'utilisateur saisit 17 centimes, l'ordinateur affichera 8 pièces de 2 centimes et 1 pièce de 1 centime.
"""
somme_centimes = int(input("Saisir une somme de centimes : "))

pieces_deux_centimes = somme_centimes // 2
pieces_un_centimes = somme_centimes % 2

print("Somme de centimes : "+str(somme_centimes))
print("Nombre de pieces de 2 centimes : "+str(pieces_deux_centimes))
print("Nombre de pieces de 1 centimes : "+str(pieces_un_centimes))
