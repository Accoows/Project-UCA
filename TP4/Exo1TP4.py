# Version flemmardise

import tkinter as tk

# On créer une fenetre
root = tk.Tk()
root.title("Arc-en-ciel")


# On créer un canvas (zone de dessin)
Hauteur = int(input('Hauteur (par défaut = 500) : '))
Largeur = int(input('Largeur (par défaut = 500) : '))
r = int(input('Rayon (par défaut = 200) : '))

Dessin = tk.Canvas(root, height=Hauteur, width=Largeur, bg="#7799FF")
Dessin.pack()


# Fonction création de disque
def disque(x, y, rayon, couleur):
    p1 = (x - rayon, y - rayon)
    p2 = (x + rayon, y + rayon)
    Dessin.create_oval(p1, p2, width=0, fill=couleur)

p = 15
disque(Largeur/2, Hauteur/2, r, '#822FC3')  # violet
r -= p
disque(Largeur/2, Hauteur/2, r, '#400072')  # violet foncé
r -= p
disque(Largeur/2, Hauteur/2, r, '#000AB4')  # bleu
r -= p 
disque(Largeur/2, Hauteur/2, r, '#00931F')  # vert
r -= p
disque(Largeur/2, Hauteur/2, r, '#D7EC00')  # jaune
r -= p
disque(Largeur/2, Hauteur/2, r, '#ECA900')  # orange
r -= p
disque(Largeur/2, Hauteur/2, r, '#EC2600')  # rouge
r -= p
disque(Largeur/2, Hauteur/2, r, '#7799FF')  # cyan

# Création du carré vert
b1 = (0, Hauteur/2)
b2 = (Largeur, Hauteur)
b = 'blue'
Dessin.create_rectangle(b1, b2, width=0, fill="#0B6400")


root.mainloop()
