from function import *
from time import *

reboot = "yes"

while reboot == "yes":
    nbr = int(input("Entrer le nombre de caractère: "))
    maj = str(input("Activer les majuscules? (yes OR no): "))
    special = str(input("Activer les caractères spéciaux? (yes OR no): "))
    ngene = int(input("Combien de clé voulez-vous générer? "))
    for i in range(ngene):
        if nbr > 0 :
            if maj == "no" and special == "no":
                print(generateAlphaNum(nbr))
            elif maj == "yes" and special == "no":
                print(genarateAlphaNumMaj(nbr))
            elif maj == "no" and special == "yes":
                print(generateAlphaNumSpe(nbr))
            elif maj == "yes" and special == "yes":
                print(generateAll(nbr))
            else:
                print("Erreur lors du saisie.")
        else:
            print("Erreur il faut au minimum 1 caractère.")
    reboot = input("Générer une nouvelle clé? (yes OR no): ")