# Exercice 6 : Pour se tester
# 1) Qu'est-ce qu’une fonction ?
""" Une fonction est un bloc de code nommé qui permet d’exécuter une ou plusieurs instructions,
souvent à partir de paramètres, et qui peut retourner une valeur. """

# 2) Comment définit-on une fonction ?
""" On utilise le mot-clé 'def' suivi du nom de la fonction et de parenthèses. """
# Exemple :
def ma_fonction():
    print("Bonjour")

# 3) Comment fait-on appel à une fonction ?
""" On écrit son nom suivi de parenthèses """
ma_fonction()

# 4) Quelle est la différence entre procédure et fonction ?
""" En Python, la distinction n’est pas formelle :
  - Une fonction retourne une valeur avec 'return'.
  - Une procédure est une fonction qui ne retourne rien (ou retourne None). """
# Exemple fonction :
def addition(a, b):
    return a + b

# Exemple procédure :
def afficher_message():
    print("Ceci est une procédure")

# 5) Comment fait-on appel à une procédure ?
""" Comme une fonction : on écrit son nom suivi de parenthèses. """
afficher_message()

# 6) Qu'est-ce qu'une variable locale ? Qu'est-ce qui la caractérise ?
""" Une variable locale est une variable déclarée à l’intérieur d’une fonction.
    Elle n’existe que pendant l’exécution de cette fonction. """
# Exemple :
def exemple():
    x = 10  # x est une variable locale à la fonction exemple()
    print(x)

# 7) Comment importe-t-on un module ?
""" On utilise le mot-clé 'import'. """
# Exemple :
import math  # permet d’utiliser des fonctions mathématiques comme math.sqrt()
print(math.sqrt(25))
