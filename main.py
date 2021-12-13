'''
3. Feladat
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
'''
from random import randrange

randomSzam = randrange(1, 5)
print("adj meg egy számot")
bemenet = int(input())
if bemenet == randomSzam:
    print("a kétszám egyezik. ")
elif bemenet > randomSzam:
    print("az általad megadot szám nagyob , mint a random szám")
else:
    print("az általad megadott szám kiseb, mint a random szám")