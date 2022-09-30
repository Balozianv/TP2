
#Victor Balozian group:403
#TP2

#importation
from random import randint
import time

#variables

chiffre = random(0,100)
nbessai = 0

#def
while True():

print("J'ai choisi un nombre entre 0 et 100. À vous de deviner...")

def victoir():
    print("BRAVO ! Bonne réponse vous avez réussi en:" nbessai " essai")
    rep = int(input("Voulez vous quitter ?" / "(y/n)"))

    if rep == n:
        main()

    if rep == y:
        print("Merci d'avoir jouer et aurevoir.")


def  main():

    print("J'ai choisi un nombre entre 0 et 100. À vous de deviner..." /)

    Essai = int(input("Entrer votre essai: "))
    print(" ")
    nbessai + 1

def analyse():

    nbessai + 1
    if Essai < chiffre:
    print("Le chiffre que vous venez de choisire est plus petit que le chiffre qui a été choisi.")
    Essai = int(input("Entrer votre essai: "))

    if Essai > chiffre:
     print("Le chiffre que vous venez de choisire est plus grand que le chiffre qui a été choisi.")
     Essai = int(input("Entrer votre essai: "))

    if Essai == chiffre:
          victoir()
