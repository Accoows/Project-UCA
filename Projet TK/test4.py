import tkinter as tk
from math import *
from random import *

################# Idee à faire #####################
# Installation d'un curseur qui multiplie le temps 
# Modification de la taille des planetes et distance avec le soleil
# Ajouter au supprimer l'apparition d'une planete
# Ajouter du texte si possible sur les planètes 
# Ajouter une zone de légende pour les planètes
# Curseur pour faire un zoom si possible en augmentant la zone de rotation et la taille des planètes
#Affichage système solaire en 2006 avec Pluton et sans pluton (2014)
###################################################

(Hauteur, Largeur) = (700, 1400)
root = tk.Tk()
root.title("Système solaire")
Dessin = tk.Canvas(root, height=Hauteur, width=Largeur, bg='black')
Dessin.pack()


class État():

    def __init__(self):
        (L, H) = (Largeur, Hauteur)
        self.étoiles = [(randint(0, L), randint(0, H)) for e in range(600)]
        self.temps = 0
        self.centre_x = Largeur // 2
        self.centre_y = Hauteur // 2
        self.rayon_base = 0

        self.modif_vitesse = 4

        ############################
        #Soleil
        self.rayon_soleil = 20
        #Mercure
        self.rayon_mercure = (self.rayon_soleil * 0.22)
        self.rayon_x_mercure = (self.rayon_soleil * 3)
        self.rayon_y_mercure = (self.rayon_soleil * 1.05)
        self.vitesse_mercure = (1 / 88) * self.modif_vitesse
        #Venus
        self.rayon_venus = (self.rayon_soleil * 0.28)
        self.rayon_x_venus = (self.rayon_soleil * 6)
        self.rayon_y_venus = (self.rayon_soleil * 1.40)
        self.vitesse_venus = (1 / 225) * self.modif_vitesse
        #Terre
        self.rayon_terre = (self.rayon_soleil * 0.3)
        self.rayon_x_terre = (self.rayon_soleil * 8)
        self.rayon_y_terre = (self.rayon_soleil * 2)
        self.vitesse_terre = (1 / 365) * self.modif_vitesse
        #Lune
        self.rayon_lune = (self.rayon_soleil * 0.1)
        self.rayon_x_lune = (self.rayon_soleil * 1.1)
        self.rayon_y_lune = (self.rayon_soleil * 0.3)
        self.vitesse_lune = (1 / 27.3) * self.modif_vitesse
        #Mars
        self.rayon_mars = (self.rayon_soleil * 0.20)
        self.rayon_x_mars = (self.rayon_soleil * 10)
        self.rayon_y_mars = (self.rayon_soleil * 3)
        self.vitesse_mars = (1 / 687) * self.modif_vitesse
        #Jupiter
        self.rayon_jupiter = (self.rayon_soleil * 0.6)
        self.rayon_x_jupiter = (self.rayon_soleil * 12)
        self.rayon_y_jupiter = (self.rayon_soleil * 4)
        self.vitesse_jupiter = (1 / 4335) * self.modif_vitesse * 10
        #Saturne
        self.rayon_saturne = (self.rayon_soleil * 0.5)
        self.rayon_x_saturne = (self.rayon_soleil * 14)
        self.rayon_y_saturne = (self.rayon_soleil * 5)
        self.vitesse_saturne = (1 / 10757) * self.modif_vitesse * 10
        #Uranus
        self.rayon_uranus = (self.rayon_soleil * 0.45)
        self.rayon_x_uranus = (self.rayon_soleil * 16)
        self.rayon_y_uranus = (self.rayon_soleil * 6)
        self.vitesse_uranus = (1 / 30687) * self.modif_vitesse * 10
        #Neptune
        self.rayon_neptune = (self.rayon_soleil * 0.45)
        self.rayon_x_neptune = (self.rayon_soleil * 18)
        self.rayon_y_neptune = (self.rayon_soleil * 7)
        self.vitesse_neptune = (1 / 60224) * self.modif_vitesse * 10
        ############################

        self.pause = False
        self.affichage()

    def affichage(self):
        Dessin.delete('all')

        #Affichage étoiles
        for (x, y) in self.étoiles:
            Dessin.create_rectangle((x - 1, y - 1), (x + 1, y + 1), fill='white')

        #Position Soleil
        (x0, y0) = (self.centre_x, self.centre_y)
        # Position de Mercure
        (x1, y1) = rotation(x0, y0, self.rayon_x_mercure, self.rayon_y_mercure, self.vitesse_mercure, self.temps)
        # Position de Venus
        (x2, y2) = rotation(x0, y0, self.rayon_x_venus, self.rayon_y_venus, self.vitesse_venus, self.temps)
        # Positions de la Terre
        (x3, y3) = rotation(x0, y0, self.rayon_x_terre, self.rayon_y_terre, self.vitesse_terre, self.temps)
        # Position de la Lune
        (x4, y4) = rotation(x3, y3, self.rayon_x_lune, self.rayon_y_lune, self.vitesse_lune, self.temps)
        # Position de Mars
        (x5, y5) = rotation(x0, y0, self.rayon_x_mars, self.rayon_y_mars, self.vitesse_mars, self.temps)
        # Position de Jupiter
        (x6, y6) = rotation(x0, y0, self.rayon_x_jupiter, self.rayon_y_jupiter, self.vitesse_jupiter, self.temps)
        # Position de Saturne
        (x7, y7) = rotation(x0, y0, self.rayon_x_saturne, self.rayon_y_saturne, self.vitesse_saturne, self.temps)
        # Position d'Uranus
        (x8, y8) = rotation(x0, y0, self.rayon_x_uranus, self.rayon_y_uranus, self.vitesse_uranus, self.temps)
        # Position de Neptune
        (x9, y9) = rotation(x0, y0, self.rayon_x_neptune, self.rayon_y_neptune, self.vitesse_neptune, self.temps)

        # Profondeur Mercure -> Soleil
        if y0 >= y1:
            disque(x1, y1, self.rayon_mercure, '#797C68')
            disque(x0, y0, self.rayon_soleil, '#ECD600')
        else:
            disque(x0, y0, self.rayon_soleil, '#ECD600')
            disque(x1, y1, self.rayon_mercure, '#797C68')
        disque(x2, y2, self.rayon_venus, '#FF4D00')
        #
        if y3 >= y4:
            disque(x4, y4, self.rayon_lune, '#A4A4A4')
        disque(x3, y3, self.rayon_terre, '#0042FF')
        if y3 < y4:
            disque(x4, y4, self.rayon_lune, '#A4A4A4')
        disque(x5, y5, self.rayon_mars, '#C80101')
        disque(x6, y6, self.rayon_jupiter, '#dc6e37')
        disque(x7, y7, self.rayon_saturne, couleur='#ffdead')
        disque(x8, y8, self.rayon_uranus, couleur='#c0d6e4')
        disque(x9, y9, self.rayon_neptune, couleur='#0049bb')


#############################################################################

#Timer
def tictac():
    if état.pause:
        état.temps += 1
    état.affichage()
    Dessin.after(10, tictac)


#Déplacement ellipse
def rotation(x, y, rayon_x, rayon_y, w, t):
    return x + rayon_x * cos(-t * w), y + rayon_y * sin(-t * w)


#Graphique planètes
def disque(x, y, r, couleur):
    p = (x + r, y + r)
    q = (x - r, y - r)
    Dessin.create_oval(p, q, fill=couleur)


#Fonction changement de taille des planètes
def modif_taille_planete(x):
    état.rayon_base = int(x)
    état.rayon_soleil = état.rayon_base

    état.rayon_mercure = (état.rayon_base * 0.22)
    état.rayon_x_mercure = (état.rayon_base * 3)
    état.rayon_y_mercure = (état.rayon_base * 1.05)

    état.rayon_venus = (état.rayon_base * 0.28)
    état.rayon_x_venus = (état.rayon_base * 6)
    état.rayon_y_venus = (état.rayon_base * 1.40)

    état.rayon_terre = (état.rayon_base * 0.3)
    état.rayon_x_terre = (état.rayon_base * 8)
    état.rayon_y_terre = (état.rayon_base * 2)

    état.rayon_lune = (état.rayon_base * 0.1)
    état.rayon_x_lune = (état.rayon_base * 1.1)
    état.rayon_y_lune = (état.rayon_base * 0.3)

    état.rayon_mars = (état.rayon_base * 0.20)
    état.rayon_x_mars = (état.rayon_base * 10)
    état.rayon_y_mars = (état.rayon_base * 3)

    état.rayon_jupiter = (état.rayon_base * 0.6)
    état.rayon_x_jupiter = (état.rayon_base * 12)
    état.rayon_y_jupiter = (état.rayon_base * 4)

    état.rayon_saturne = (état.rayon_base * 0.5)
    état.rayon_x_saturne = (état.rayon_base * 14)
    état.rayon_y_saturne = (état.rayon_base * 5)

    état.rayon_uranus = (état.rayon_base * 0.45)
    état.rayon_x_uranus = (état.rayon_base * 16)
    état.rayon_y_uranus = (état.rayon_base * 6)

    état.rayon_neptune = (état.rayon_base * 0.45)
    état.rayon_x_neptune = (état.rayon_base * 18)
    état.rayon_y_neptune = (état.rayon_base * 7)

    état.affichage()


#Fonction de pause (stop)
def pause(event):
    état.pause = not état.pause


#Curseur d'agrandissement
# curseur_taille = tk.Scale(root, orient="horizontal", length=Largeur,
#                           label='Taille', command=modif_taille_planete,
#                           from_=20, to=60)
#
# curseur_taille.pack(side="left")

def settings():
    win = tk.Toplevel()
    win.title("Settings")
    win.geometry("400x400")
    (Hauteur, Largeur) = (400, 400)
    curseur_taille = tk.Scale(win, orient="horizontal" ,length=Largeur,
                              label='Taille', command=modif_taille_planete,
                              from_=20, to=35)

    curseur_taille.pack(side="left")


Btn_settings = tk.Button(root, text='Settings', width=9, command=settings)
Btn_settings.pack()

état = État()
tictac()
root.bind('<space>', pause)
root.mainloop()
