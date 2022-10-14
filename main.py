
#Victor Balozian group:403
#TP2

#importation
from random import randint
import time

#variables
chiffre = randint(0, 100)
nbtry = 0
boucle_jeu = True


while boucle_jeu:

   #main
   plimite = int(input("Sélectionner la limite du plus petite nombre: \n"))
   glimite = int(input("Sélectionner la limite du plus Grand nombre: \n"))

   chiffre = randint(plimite, glimite)

   print("J'ai choisi un nombre entre ",plimite, " et ",glimite, ". À vous de deviner...")
   essai = int(input("Entrer votre essai: \n"))
   essai_faux = True

   while essai_faux:

       #ananylse
       if essai < chiffre:
           print("\nLe chiffre que vous venez de choisire est plus petit que le chiffre qui a été choisi.")
           essai = int(input("Entrer votre essai: "))

       if essai > chiffre:
           print("\nLe chiffre que vous venez de choisire est plus grand que le chiffre qui a été choisi.")
           essai = int(input("Entrer votre essai: "))
           nbtry = +1

       if essai == chiffre:

           nbtry = +1
           print("BRAVO ! Bonne réponse vous avez réussi en seulment:", nbtry, " essai")

           rep = input("Voulez vous quitter ? \n (y/n)")
           if rep == "n":
               essai_faux = False

           if rep == "y":
               print("Merci d'avoir jouer et aurevoir.")
               essai_faux = False
               boucle_jeu = False