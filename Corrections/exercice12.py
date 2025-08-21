# Exercice 12 : Cinéma
"""
Une place dans un cinéma coûte 5 euros pour les moins de 10 ans,
6 euros pour les moins de 18 ans et 8 euros pour les autres.
Écrire une procédure prix qui prend en paramètre un âge et affiche le prix correspondant.
"""
age = 12
def prix(age):
    if(age < 10):
        print("Tu as " + str(age) + " ans alors la place de cinéma coûte 5 euros")
    elif(age < 18):
        print("Tu as " + str(age) + " ans alors la place de cinéma coûte 6 euros")
    else:
        print("Tu as " + str(age) + " ans alors la place de cinéma coûte 8 euros")

prix(age)
