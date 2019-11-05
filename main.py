import numpy as np
import tkinter as tk
from tkinter import *


print("Init")
print("")
#Création d'un matrice 5x6 avec un dant integer (1 à 5)
matrice = np.random.randint(1,5,size=(5,6))
ROWS=5
COLS=6
size = 40
can_width = 800
can_height = 600
can_width = size * ROWS
can_height = size * COLS
print("")
print(matrice)
print()
print(np.size(matrice))
print(np.shape(matrice))
print(np.ndim(matrice))
print(np.mean(matrice))
print()
print(matrice[0,0])
print("test")
aaa = np.size(matrice)
print(aaa)
couleurs = {5: "white", 1: "blue", 2: "red", 3: "green", 4: "black"}


#Ma fenetre tkinter
window = tk.Tk()

# Création d'un widget Label (texte 'Bonjour tout le monde !')
Label1 = Label(window, text = 'Matrice :', fg = 'red')

# Positionnement du widget avec la méthode pack()
Label1.pack()



#Création d'un canvas afin de mettre des rectangles dedans.
canvas = Canvas(window, width=can_width, height=can_height)
canvas.pack()

#Création d'un carré dans la canvas crée précédemment.
#carr1 = canvas.create_rectangle(0, 0, size, size, fill='red')
#for i in range(np.size(matrice)):
#    print(i)
#    canvas.create_rectangle(i*size, i*size, i*size + size, i*size +size, fill='blue')

for r in range(ROWS):
    print(r)
    rsize=(r*size)
    for i in range(COLS):
        print("i = " + str(i) + " r = " + str(r))
        print(matrice[r,i])
        print(couleurs[1])
        isize=(i*size)
        #couleurs(1)
        canvas.create_rectangle(isize, rsize, isize + size, rsize + size, fill = couleurs[matrice[r,i]])




        
#canvas.move(carr1, 20, 20)



# Création d'un widget Button (bouton Quitter)
Bouton1 = Button(window, text = 'Quitter', command = window.destroy)
Bouton1.pack()






window.mainloop()

