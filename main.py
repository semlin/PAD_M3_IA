import numpy as np
import tkinter as tk
from tkinter import *

class Matrice:

	#Ma classe matrice classe matrice
	def __init__(self):
		self._nom:"Matrice"
		self._colones:6
		self._lignes:5

	#Accesseur colones classe matrice
	@property
    def colones(self):
        print "Récupération du nombre de colones"
        return self._colones

    #Setter colones classe matrice
    @colones.setter
    def colones(self, v):
        print "Changement du nombre de colones"
        self._colones  =  v	

    #Accesseur lignes classe matrice
	@property
    def lignes(self):
        print "Récupération du nombre de lignes"
        return self._lignes

    #Setter lignes classe matrice
    @lignes.setter
    def lignes(self, v):
        print "Changement du nombre de lignes"
        self._lignes  =  v	



ma_matrice = Matrice()
























#Création d'un matrice 5x6 avec un dant integer (1 à 5)
# matrice = np.random.randint(1,5,size=(5,6))
# ROWS=5
# COLS=6
# size = 40
# can_width = size * ROWS
# can_height = size * COLS

#Mémo des commande usefull en matrice.
# print(matrice)
# print(np.size(matrice))
# print(np.shape(matrice))
# print(np.ndim(matrice))
# print(np.mean(matrice))
# print(matrice[0,0])

# couleurs = {5: "white", 1: "blue", 2: "red", 3: "green", 4: "black"}

#Ma fenetre tkinter
# window = tk.Tk()

# Création d'un widget Label (texte 'Bonjour tout le monde !')
# Label1 = Label(window, text = 'Matrice :', fg = 'red')

# Positionnement du widget avec la méthode pack()
# Label1.pack()


#Création d'un canvas afin de mettre des rectangles dedans.
# canvas = Canvas(window, width=can_width, height=can_height)
# canvas.pack()

#Création d'un boucle pour générer le tableau de carré et fill en fonction de la valeur.
#Itération sur r qui représente les lignes et i qui représente les colones.
# for r in range(ROWS):
#     print(r)
#     rsize=(r*size)
#     for i in range(COLS):
#         print("i = " + str(i) + " r = " + str(r))
#         print(matrice[r,i])
#         print(couleurs[1])
#         isize=(i*size)
#         canvas.create_rectangle(isize, rsize, isize + size, rsize + size, fill = couleurs[matrice[r,i]])

# Création d'un widget Button (bouton Quitter)
# Bouton1 = Button(window, text = 'Quitter', command = window.destroy)
# Bouton1.pack()


window.mainloop()