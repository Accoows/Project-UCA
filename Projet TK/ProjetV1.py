import tkinter as tk
from math import *
from random import *


################# Idee à faire #####################
# Installation d'un curseur qui multiplie le temps 
# Choix d'un systeme solaire verticale ou horizontale
# Modification de la taille des planetes
# Ajouter au supprimer l'apparition d'une planete
# Ajouter du texte si possible sur les plantes 
# Ajouter une zone de légende pour les planètes
# Curseur pour faire un zoom si possible en augmentant la zone de rotation et la taille des planètes
###################################################

(Hauteur, Largeur) = (700, 1400)
root = tk.Tk()
root.title("Système solaire (sans png)")
Dessin = tk.Canvas(root, height=Hauteur, width=Largeur, bg='black')
Dessin.pack()

class État():
    
    def __init__(self):
        (L, H) = (Largeur, Hauteur)
        self.étoiles = [(randint(50, L), randint(50, H)) for e in range(300)]
        self.temps = 0
        self.centre_x = Largeur//2
        self.centre_y = Hauteur//2
        self.rayon_base = 0
        self.rayon_terre = 20 ; self.rayon_lune = 5 ; self.rayon_soleil = 60 ; self.rayon_mercure = 20
        self.rayon_x_terre = 200 ; self.rayon_y_terre = 40
        self.rayon_x_lune = 80 ; self.rayon_y_lune = 12
        self.rayon_x_mercure = 150 ; self.rayon_y_mercure = 40
        self.vitesse_terre = 1/365 ; self.vitesse_lune = 1/27.3 ; self.vitesse_mercure = 1/88
        self.pause = False
        self.affichage()
        
    def affichage(self):
        Dessin.delete('all')
        
        #Affichage étoiles
        for (x, y) in self.étoiles:
            Dessin.create_rectangle((x-1, y-1), (x+1, y+1), fill='white')
        
        #Position Soleil
        (x0, y0) = (self.centre_x, self.centre_y)
        
        # Positions de la Terre et de la Lune
        (x1, y1) = rotation(x0, y0, self.rayon_x_terre, self.rayon_y_terre, self.vitesse_terre, self.temps)
        (x2, y2) = rotation(x1, y1, self.rayon_x_lune, self.rayon_y_lune, self.vitesse_lune, self.temps)

        # Position de Mercure
        (x3, y3) = rotation(x0, y0, self.rayon_x_mercure, self.rayon_y_mercure, self.vitesse_mercure, self.temps)
        
        # Profondeur de la Terre/Lune par rapport au Soleil
        if y1 >= y0:                                         # Terre en bas de l'ellipse du Soleil
            disque(x0, y0, self.rayon_soleil, '#ECD600')      # Soleil par-dessus tout
            if y1 >= y2:                                     # Lune en bas de l'ellipse de la Terre
                disque(x2, y2, self.rayon_lune, '#A4A4A4')      # Lune ensuite
            disque(x1, y1, self.rayon_terre, 'blue')         # Terre d'abord                
            if y1 < y2:                                      # Lune en haut de l'ellipse de la Terre
                disque(x2, y2, self.rayon_lune, '#A4A4A4')      # Lune derrière la Terre
        else:                                                # Terre en haut de l'ellipse du Soleil
            disque(x0, y0, self.rayon_soleil, '#ECD600')      # Soleil par-dessus tout
            if y1 >= y2:                                     # Lune en bas de l'ellipse de la Terre
                disque(x2, y2, self.rayon_lune, '#A4A4A4')      # Lune devant la Terre
            disque(x1, y1, self.rayon_terre, 'blue')         # Terre par-dessus le Soleil
            disque(x0, y0, self.rayon_soleil, '#ECD600')      # Soleil par-dessus la Terre
            if y1 < y2:                                      # Lune en haut de l'ellipse de la Terre
                disque(x2, y2, self.rayon_lune, '#A4A4A4')      # Lune derrière la Terre
                disque(x0, y0, self.rayon_soleil, '#ECD600')  # Soleil devant la lune

        if y0 >= y3:
            disque(x3, y3, self.rayon_mercure, '#797C68')
            disque(x0, y0, self.rayon_soleil, '#ECD600')
        else:
            disque(x0, y0, self.rayon_soleil, '#ECD600')
            disque(x3, y3, self.rayon_mercure, '#797C68')
            
            
#Timer
def tictac():
    if not état.pause:
        état.temps += 1
    état.affichage()
    Dessin.after(20, tictac)
    
#Déplacement ellipse
def rotation(x, y, rayon_x, rayon_y, w, t):
    return (x + rayon_x * cos(-t * w), y + rayon_y * sin(-t * w))

#Graphique planètes
def disque(x, y, r, couleur):
    p = (x + r, y + r)
    q = (x - r, y - r)
    Dessin.create_oval(p, q, fill=couleur)

#Fonction changement de taille des planètes
def modif_taille_planete(x):
    état.rayon_base = int(x)
    état.rayon_soleil = état.rayon_base
    état.rayon_terre = état.rayon_base // 4
    état.rayon_lune = état.rayon_base // 6
    état.rayon_mercure = état.rayon_base // 4
    état.affichage()

#Fonction de pause (stop)
def pause(event):
    état.pause = not état.pause

#Curseur d'aggrandissement   
curseur_systeme = tk.Scale(root, orient="horizontal", length=Largeur,
                        label='Taille',command=modif_taille_planete,
                        from_=20, to=100)

curseur_systeme.pack(side="left")



état = État()
tictac()
root.bind('<space>', pause)
root.mainloop()