
# Exercice 10 : Conversion durée
"""
Écrire une procédure conv_duree prenant en paramètre une durée en secondes puis affichant cette même durée en heures, minutes et secondes.
"""
duree_totale = 7422

def conv_duree(pDuree):
    heures = pDuree//3600
    minutes = (pDuree%3600) // 60
    secondes = pDuree%60
    return heures, minutes, secondes

heures, minutes, secondes = conv_duree(duree_totale)

print("Durée totale : " + str(duree_totale) + "secondes => " + str(heures) + "h" + str(minutes) + "min" + str(secondes) +"sec")