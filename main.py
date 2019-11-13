import numpy as np
import tkinter as tk
from tkinter import *

class Matrice:

    #Ma classe matrice
    def __init__(self):
        self.nom = "Matrice"
        self._colones = 6
        self._lignes= 5
        self._values= np.random.randint(1,5,size=(self._lignes,self._colones))

    #Accesseur colones classe matrice
    @property
    def colones(self):
        print ("Récupération du nombre de colones")
        return self._colones

    #Setter colones classe matrice
    @colones.setter
    def colones(self, v):
        print ("Changement du nombre de colones")
        self._colones  =  v 

    #Accesseur lignes classe matrice
    @property
    def lignes(self):
        print ("Récupération du nombre de lignes")
        return self._lignes

    #Setter lignes classe matrice
    @lignes.setter
    def lignes(self, v):
        print ("Changement du nombre de lignes")
        self._lignes  =  v  

    #Accesseur values classe matrice
    @property
    def values(self):
        print ("Récupération des valeurs")
        return self._values

    #Setter lignes classe matrice
    @values.setter
    def values(self, v):
        print ("Changement des valeurs")
        self._values  =  v  

ma_matrice = Matrice()

#print(ma_matrice.nom, ma_matrice.colones, ma_matrice.lignes)
#print(ma_matrice.values)

#Taille d'une célulle de la matrice.
size = 40
can_width = size * ma_matrice.lignes
can_height = size * ma_matrice.colones

#Mémo des commandes usefull.
# print(ma_matrice.values)
# print(np.size(ma_matrice.values))
# print(np.shape(ma_matrice.values))
# print(np.ndim(ma_matrice.values))
# print(np.mean(ma_matrice.values))
# print(ma_matrice.values[0,0])

couleurs = {5: "white", 1: "blue", 2: "red", 3: "green", 4: "black"}

# Ma fenetre tkinter
window = tk.Tk()

# Création d'un widget Label.
Label1 = Label(window, text = 'Matrice :', fg = 'red')
# Positionnement du widget avec la méthode pack()
Label1.pack()


# Création d'un canvas afin de mettre des rectangles(carré du coup) dedans.
canvas = Canvas(window, width=can_width, height=can_height)
canvas.pack()

# Création d'une boucle pour générer le tableau de carrés et fill en fonction de la valeur matricielle associée.
# Itération sur r qui représente les lignes et i qui représente les colones.
for r in range(ma_matrice.lignes):
    # rsize augmente à chaque itération afin de décaler chaque nouveau block)
    # On retrouve le même type d'itération pour les colones avec le isize ci-dessous
    rsize=(r*size)
    for i in range(ma_matrice.colones):
        isize=(i*size)
        canvas.create_rectangle(isize, rsize, isize + size, rsize + size, fill = couleurs[ma_matrice.values[r,i]])

# Création d'un widget Button (bouton Quitter)
Bouton1 = Button(window, text = 'Quitter', command = window.destroy)
Bouton1.pack()


window.mainloop()
